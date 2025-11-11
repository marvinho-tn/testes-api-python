from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

item_id_param = openapi.Parameter(
    'item_id', openapi.IN_PATH, description="Item Id", type=openapi.TYPE_INTEGER, required=True
)
q_param = openapi.Parameter(
    'q', openapi.IN_QUERY, description="Optional query string", type=openapi.TYPE_STRING
)

# Endpoint para obter detalhes de um item
@swagger_auto_schema(
    method='get',
    operation_summary="Read Item",
    manual_parameters=[item_id_param, q_param],
    responses={200: "Successful Response", 422: "Validation Error"}
)
@api_view(['GET'])
def detail_view(request, item_id: int):
    query = request.GET.get("q")
    return Response({
        "id": item_id,
        "query": query
    })
