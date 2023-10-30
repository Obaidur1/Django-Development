from django.urls import path
from .views import add_property_view, add_property_view2

urlpatterns = [
    path("", add_property_view, name="add_property"),
]
