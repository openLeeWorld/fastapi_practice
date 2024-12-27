from fastapi import APIRouter, HTTPException
from model.creature import Creature
import os
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service
else:
    from service import creature as service
from error import Missing, Duplicate
    
router = APIRouter(prefix="/creature")

@router.get("")
@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    
@router.post("/", status_code=201)
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)

@router.patch("/{name}")
def modify(name, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.put("/{name}")
def replace(name, creature: Creature) -> Creature:
    try:
        return service.replace(name, creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{name}")
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

"""
plotly로 점도표 테스트 엔드포인트를 추가한다.
"""
from fastapi import Response
import plotly.express as px

@router.get("/test/")
def test():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")

"""
생명체 이름 이니셜이 있는 막대 차트
"""
from collections import Counter
from service.creature import get_all

@router.get("/plot/")
def plot():
    creatures = get_all()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts = Counter(creature.name[0] for creature in creatures)
    y = { letter: counts.get(letter, 0) for letter in letters}
    fig = px.histogram(x=list(letters), y=y, title="Creature Names",
                        labels={"x": "Initial", "y": "Initial"})
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")

""" 
크립티드가 있는 국가지도(Choropleth: 어떤 기준에 의해 영역별 색상이 다르게 보이는 지도)를 그린다.
"""
import country_converter as coco

@router.get("/map/")
def map(): 
    creatures = service.get_all()
    iso2_codes = set(creature.country for creature in creatures)
    iso3_codes = coco.convert(names=iso2_codes, to="ISO3")
    # db에 저장된 iso 2글자 코드를 coco에서 쓰는 iso 3글자 코드로 변환한다.
    fig = px.choropleth(
        locationmode="ISO-3",
        locations=iso3_codes
    )
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")


"""
country가 US인 경우, 두 문자로 된 주 코드인 area필드를 사용해서 이 맵을 확장해 미국에 초점을 맞춘다.
locationmode="USA-states"로 설정하고 px,choropleth()의 locations에 할당한다.
"""
@router.get("/map2/")
def map2():
    creatures = service.get_all()
    areas = [creature.area for creature in creatures]
    fig = px.choropleth(
        locationmode="USA-states",
        locations=areas
    )
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")