from fastapi import FastAPI, Body, Header, Response

app = FastAPI() # 전체 웹 애플리케이션을 나타내는 최상위 FastAPI 객첸

@app.get("/hi") # ? 파라미터로 전달(여러개 일 시 &로 전달)
def greet1(who):
    return f"Hello {who}"

@app.get("/hi/{who}") # 경로 데코레이터로 파라미터 전달
def greet2(who):
    return f"Hello {who}"

@app.post("/hi") # body json으로 전달
def greet3(who: str = Body(embed=True)):
    return f"Hello {who}"

@app.get("/agent") # 파라미터 헤더로 전달
def get_agent(user_agent: str = Header()):
    return user_agent

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
# url "/hi"에 대한 요청, HTTP GET에만 적용