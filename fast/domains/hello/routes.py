from fastapi import APIRouter
from shared.domains.hello.services import HelloService

router = APIRouter()

# Endpoint de hello world
@router.get("/")
def hello_world():
    return HelloService.get_greeting()