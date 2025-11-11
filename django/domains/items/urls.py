from django.urls import path
from .views import detail_view

urlpatterns = [
    path("<int:item_id>/", detail_view, name="detail"),
]
