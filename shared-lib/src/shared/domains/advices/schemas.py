from pydantic import BaseModel

class AdviceRead(BaseModel):
    id: int
    advice: str

class AdviceCountRead(BaseModel):
    count: int