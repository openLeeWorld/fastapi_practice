from fastapi import FastAPI
app = FastAPI()

"""
FastAPI로 작은 파일 업로드 처리하기
"""
from fastapi import File

@app.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"
# http -f 로 --form을 포함해야 한다.
# http -f -b POST http://localhost:8000/small small_file@1KB.bin

"""
FastAPI로 큰 파일 업로드 처리하기
"""
from fastapi import UploadFile

@app.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"
# http -f -b POST http://localhost:8000/big big_file@1KB.bin

"""
FileResponse를 사용하여 작은 파일 다운로드하기
"""
from fastapi.responses import FileResponse

@app.get("/small/{name}")
async def download_small_file(name: str) -> FileResponse:
    return FileResponse(name)

"""
StreamingResponse를 사용하여 큰 파일 다운로드하기
"""
from typing import Generator
from fastapi.responses import StreamingResponse

def gen_file(path: str) -> Generator:
    try:
        with open(file=path, mode="rb") as file:
            yield file.read()
    except FileNotFoundError:
        yield b"File not found"
    except Exception as e:
        yield str(e).encode()
        
@app.get("/download_big/{name}")
async def download_big_file(name: str):
    gen_expr = gen_file(path=name)
    first_chunk = next(gen_expr)
    if first_chunk == b"File not found":
        return {"error": "File not found"}
    elif first_chunk.startswith(b"Exception:"):
        return {"error": first_chunk.decode()}
    response = StreamingResponse(
        content=gen_expr,
        status_code=200,
    )
    return response

"""StaticFiles를 사용해 디렉터리의 모든 것을 제공"""
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)