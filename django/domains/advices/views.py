from django.http import JsonResponse
from shared.domains.advices.external_service import ExternalAdviceService
from shared.domains.advices.schemas import AdviceRead

def advice_view(request):
    advice = ExternalAdviceService.get_advice()
    advice_read = AdviceRead(
        id=advice.slip.id,
        advice=advice.slip.advice
    )
    return JsonResponse(advice_read.dict())
