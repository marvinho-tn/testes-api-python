from domains.advices.serializes import AdviceCountSerializer, AdviceSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shared.domains.advices.external_service import ExternalAdviceService
from shared.domains.advices.schemas import AdviceRead
from shared.domains.advices.service import AdviceService

@swagger_auto_schema(
    method='get',
    operation_summary="Get Advice",
    responses={200: AdviceSerializer}
)
@api_view(['GET'])
def advice_view(request):
    advice = ExternalAdviceService.get_advice()
    response = AdviceRead(
        id=advice.slip.id,
        advice=advice.slip.advice
    )
    return Response(response.dict())

@swagger_auto_schema(
    method='get',
    operation_summary="Get Advice Count",
    responses={200: AdviceCountSerializer}
)
@api_view(['GET'])
def advice_count_view(request):
    service = AdviceService()
    response = service.get_advice_count()
    return Response(response.dict())
