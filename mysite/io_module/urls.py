from django.urls import path
from .views import IOModuleView
from .serializers import IOModuleSerializer
app_name = 'io'

urlpatterns = [
    path("", IOModuleView.as_view(), name="io"),
    path("<int:pk>/", IOModuleView.as_view(), name="io")
    # path("", IOModuleSerializer, name="io")
]
