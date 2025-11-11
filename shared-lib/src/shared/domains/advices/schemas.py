from pydantic import BaseModel

# Classe de esquema para leitura de conselhos
class AdviceRead(BaseModel):
    id: int
    advice: str

# Classe de esquema para leitura da contagem de conselhos
class AdviceCountRead(BaseModel):
    count: int