from fastapi import APIRouter
from shared.domains.hello.services import HelloService

router = APIRouter()

@router.get("/")
def hello_world():
    return HelloService.get_greeting()