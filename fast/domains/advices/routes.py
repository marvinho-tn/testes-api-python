from fastapi import APIRouter
from shared.domains.advices.external_service import ExternalAdviceService
from shared.domains.advices.schemas import AdviceCountRead, AdviceRead
from shared.domains.advices.service import AdviceService

router = APIRouter()

# Endpoint de busca de um conselho aleatório
@router.get("/", response_model=AdviceRead)
def get_advice():
    advice = ExternalAdviceService.get_advice()
    return AdviceRead(
        id=advice.slip.id,
        advice=advice.slip.advice
    )

# Endpoint de quantidade de conselhos buscados
@router.get("/count", response_model=AdviceCountRead)
def get_advice_count():
    service = AdviceService()
    read = service.get_advice_count()
    return read