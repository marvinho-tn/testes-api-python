from .views import detail_view
from django.urls import path

urlpatterns = [
    path("<int:item_id>/", detail_view, name="detail"),
]
