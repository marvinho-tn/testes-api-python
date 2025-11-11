from django.http import HttpResponse
from shared.domains.hello.services import HelloService
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_summary="Hello World",
    responses={200: "Successful Response"}
)
@api_view(['GET'])
def hello_view(request):
    message = HelloService.get_greeting()
    return Response(message)

