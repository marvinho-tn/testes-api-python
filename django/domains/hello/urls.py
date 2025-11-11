from .views import hello_view
from django.urls import path

# Lista de URLs do domínio de hello
urlpatterns = [
    path("", hello_view, name="hello"),
]
