from django.urls import path
from .views import IOModuleView

app_name = 'io'

urlpatterns = [
    path("", IOModuleView.as_view(), name="io")
]
