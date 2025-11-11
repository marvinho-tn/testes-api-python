from django.urls import path
from .views import advice_count_view, advice_view

urlpatterns = [
    path("", advice_view, name="advices"),
    path("count/", advice_count_view, name="advice-count"),
]
