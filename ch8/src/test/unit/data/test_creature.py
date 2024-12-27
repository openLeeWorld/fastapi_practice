import os
import pytest
from model.creature import Creature
from error import Missing, Duplicate

# 아래 줄에 있는 data.init에 메모리 DB를 사용하도록 data모듈을 가져오기 전에 설정한다.
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
# SQLite가 기존 db파일을 손상시키거나 디스크에 파일을 생헝하지 않고 메모리에서 작동 가능
# data 모듈이 중복돼 explorer를 찾지 못해 src를 명시한다.
from src.data import creature

@pytest.fixture # 테스트에서 재사용할 데이터를 생성하고 전달하는 기능을 제공합니다.
def sample() -> Creature:
    return Creature(name="Yeti", country="CN", area="Himalayas",
            description="Harmless Himalayan",
            aka="Abominable Snowman")
# 이전 함수의 변경사항이 지속됨(함수 스코프)
def test_create(sample): # 테스트할 함수에 인수로 fixture를 제공하면 샘플 데이터로 변환됨
    resp = creature.create(sample)
    assert resp == sample
    
def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)
        
def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample
    
def test_modify2(sample):
    creature.country = "JP"
    resp = creature.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing2():
    thing: Creature = Creature(name="snurfle",
        description="some thing", country="somewhere", area="*", aka="*")
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)
    
def test_get_one_missing():
    with pytest.raises(Missing):
        _ = creature.get_one("boxturtle")
        
def test_modify(sample):
    creature.area = "Sesame Street"
    resp = creature.modify(sample.name, sample)
    assert resp == sample
    
def test_modfiy_missing():
    thing: Creature = Creature(name="snurfle", country="RU", area="",
                            description="some thing", aka="")

    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)
        
def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp == True
    
def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)
    