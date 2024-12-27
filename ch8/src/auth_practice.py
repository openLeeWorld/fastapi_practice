import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

maybe: str = "whodis?"
user: str = "newphone"


basic: HTTPBasicCredentials = HTTPBasic() # 아이디, 비번의 기본 인증

@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if (creds.username == user and 
        creds.password == maybe):
        return {"username": creds.username, "password": creds.password}
    
    raise HTTPException(status_code=401, detail="Hey!")

if __name__ == "__main__":
    uvicorn.run("auth:app", reload=True)

