from django.urls import path
from io_module.views import LCIOModuleAPI, RUDIOModuleAPI
from .serializers import IOModuleSerializer
app_name = 'io'

urlpatterns = [
    # path("", IOModuleView.as_view(), name="io"),
    # path("<int:pk>/", IOModuleView.as_view(), name="io")
    path("", LCIOModuleAPI.as_view(), name="io"),
    path("<int:pk>", RUDIOModuleAPI.as_view(), name="io"),
]
