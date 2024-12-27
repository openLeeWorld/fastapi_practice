from pydantic import BaseModel, StringConstraints, Field
from typing import Annotated

# 생명체 모델 정의(db schema)
class Creature(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    country: Annotated[str, Field(min_length=2, max_length=100)]
    area: str
    description: str
    aka: str
    
thing = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman"
)

print("Name is", thing.name)