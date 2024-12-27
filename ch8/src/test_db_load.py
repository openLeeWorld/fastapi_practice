from faker import Faker
from time import perf_counter

def load():
    from error import Duplicate
    from data.explorer import create
    from model.explorer import Explorer
    
    f = Faker() # 미리 준비된 목록으로 이름 생성
    NUM = 100_000
    t1 = perf_counter()
    for row in range(NUM):
        try:
            create(Explorer(name=f.name(),
                country=f.country(),
                description=f.text()))
        except Duplicate: # 이름이 중복되면 무시한다.
            pass
    t2 = perf_counter()
    print(NUM, "rows")
    print("write time:", t2-t1)
    
def read_db():
    from data.explorer import get_all
    t1 = perf_counter()
    _ = get_all()
    t2 = perf_counter()
    print("db read time:", t2-t1)
    
def read_api():
    from fastapi.testclient import TestClient
    from main import app
    t1 = perf_counter()
    client = TestClient(app)
    _ = client.get("/explorers")
    t2 = perf_counter()
    print("api read time:", t2-t1)
    
load()
read_db()
read_db() # sqlite가 쿼리를 준비하는 시간을 없애기 위해 두 번 호출
read_api()
    
"""
결과: 
100000 rows
write time: 42.01955119986087
db read time: 0.3140713998582214
db read time: 0.4062848000321537
api read time: 0.012260599993169308
"""