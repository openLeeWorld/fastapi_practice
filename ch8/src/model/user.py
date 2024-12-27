from pydantic import BaseModel

class PublicUser(BaseModel): 
    name: str # 외부로 노출되는 유일한 속성
    
class SignInUser(PublicUser):
    password: str # 유저가 처음 가입시 사용하는 암호
    
class PrivateUser(PublicUser):
    hash: str # 비밀번호를 암호화한 값
    
