from django.http import HttpResponse
from shared.domains.hello.services import HelloService

def hello_view(request):
    message = HelloService.get_greeting()
    return HttpResponse(message)

