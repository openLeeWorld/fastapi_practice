from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str # 두 문자로 된 ISO 국가 코드
    area: str
    description: str
    aka: str