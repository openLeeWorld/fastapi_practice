from datetime import datetime
from pydantic import BaseModel

class TagIn(BaseModel): # 사용자가 제공해야 하는 정보
    tag: str
    
class Tag(BaseModel): # 태그 클래스
    tag: str
    created: datetime # 태그가 생성된 시점
    secret: str # 데이터 베이스에 저장, 외부 노출x
    
class TagOut(BaseModel): # 사용자 반환 항목
    tag: str
    created: datetime

