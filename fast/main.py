from domains.advices.routes import router as advices_router
from domains.hello.routes import router as hello_router
from fastapi import FastAPI

# Cria a aplicação FastAPI
app = FastAPI()

# Rota com parâmetro
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

app.include_router(hello_router, tags=["hello"])
app.include_router(advices_router, prefix="/advices", tags=["advices"])