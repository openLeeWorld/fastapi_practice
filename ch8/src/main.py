from fastapi import FastAPI
from web import explorer, creature, user, game 
# 절대 경로 import
# 상대 경로 import(.web)시에는 스크립트 실행이 아니라 모듈이 파이썬 패키지의 일부여야 함

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)
app.include_router(game.router)

# 현재 FastAPI는 파이썬 3.11이 기본으로 제공하는 OAS(3.1.0)을 지원하지 않는다.
# 따라서 OAS 문서가 더 낮은 버전으로 생성되도록 main.py를 수정한다.
# FastAPI는 OAS 3.0.2를 지원한다.
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI OAS 3.0.2",
        version="3.0.2",
        openapi_version="3.0.2",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
    #uvicorn.run("main:app", host="localhost", port=8000, reload=True)