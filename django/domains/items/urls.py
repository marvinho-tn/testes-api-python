from .views import detail_view
from django.urls import path

# Lista de URLs do domínio de items
urlpatterns = [
    path("<int:item_id>/", detail_view, name="detail"),
]
