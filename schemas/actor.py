from pydantic import BaseModel, Field
from typing import Optional 

class Actor(BaseModel):
    id: Optional[int] = None
    fname: str = Field(max_length=30,min_length=3)
    lname: str = Field(max_length=20,min_length=3)
    gender: str = Field(max_length=10,min_length=1)

    class Config:
        schema_extra = {
            "example": {
                'id': 1,
                'fname': 'Johnny',
                'lname': 'Depp',
                'gender': 'fantasy'
            }
        }