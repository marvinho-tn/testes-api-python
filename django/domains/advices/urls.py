from django.urls import path
from .views import advice_view

urlpatterns = [
    path("", advice_view, name="advices"),
]
