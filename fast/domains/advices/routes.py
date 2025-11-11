from fastapi import APIRouter
from shared.domains.advices.external_service import ExternalAdviceService
from shared.domains.advices.schemas import AdviceRead

router = APIRouter()

# Endpoint de busca de um conselho aleatório
@router.get("/", response_model=AdviceRead)
def get_advice():
    advice = ExternalAdviceService.get_advice()
    return AdviceRead(
        id=advice.slip.id,
        advice=advice.slip.advice
    )