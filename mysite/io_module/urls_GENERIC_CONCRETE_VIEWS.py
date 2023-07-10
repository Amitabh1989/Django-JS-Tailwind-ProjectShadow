from django.urls import path
from io_module import views
from .serializers import IOModuleSerializer
app_name = 'io'

urlpatterns = [
    # path("", views.IOModuleListAPI.as_view(), name="io"),
    path("", views.IOModuleCreateAPI.as_view(), name="io"),
    path("<int:pk>/", views.IOModuleRetrieveAPI.as_view(), name="io"),
    # path("", views.IOModuleListAPI.as_view(), name="io"),
    # path("", views.IOModuleListAPI.as_view(), name="io"),
]
