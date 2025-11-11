from pydantic import BaseModel

class AdviceRead(BaseModel):
    id: int
    advice: str