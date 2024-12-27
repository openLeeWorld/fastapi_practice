from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/who2")
def greet2(name: str = Form()):
    return f"Hello, {name}!"

from pathlib import Path
from fastapi.staticfiles import StaticFiles

# main.py가 포함된 디렉터리
top = Path(__file__).resolve().parent

"""
/static 경로에 대한 요청을 처리합니다.
top/static 디렉터리에 있는 파일들을 제공하도록 설정합니다.
html=True 옵션을 사용하여 디렉터리 인덱스를 활성화합니다.
이 마운트된 경로의 이름을 "free"로 지정합니다.
따라서, /static 경로로 들어오는 요청은 top/static 디렉터리에서 해당 파일을 찾아 제공하게 됩니다.
"""
app.mount("/static",
        StaticFiles(directory=f"{top}/static", html=True),
        name="free")

@app.post("/who2") # form은 post로 전달해야 한다.
def greet3(name: str = Form()):
    return f"Hello, {name}!"

""" 템플릿 구성 및 사용 예시"""
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates_obj = Jinja2Templates(directory=f"{top}/template")
# 미리 정의된 친구들 목록을 가져옴
from fake.creature import _creatures as fake_creatures
from fake.explorer import _explorers as fake_explorers

@app.get("/list")
def explorer_list(request: Request):
    return templates_obj.TemplateResponse("list.html",
            {"request": request, "creatures": fake_creatures, "explorers": fake_explorers})
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)