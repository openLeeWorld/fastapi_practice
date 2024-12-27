from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(2) # db호출이나 웹 페이지 다운로드 등 다른 거 실행
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run("greet_async:app", reload=True)
