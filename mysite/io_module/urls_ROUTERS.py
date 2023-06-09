from django.urls import path, include
from io_module import views
from .serializers import IOModuleSerializer
from rest_framework.routers import DefaultRouter
app_name = 'io'

router = DefaultRouter()

router.register("io", views.IOModuleViewSet, basename="io")

urlpatterns = [
    # path("", views.IOModuleListAPI.as_view(), name="io"),
    # path("", views.IOModuleViewSet.as_view(), name="io"),
    # path("<int:pk>/", views.IOModuleRetrieveUpdateDestroyAPI.as_view(), name="io"),
    # path("", views.IOModuleListAPI.as_view(), name="io"),
    # path("", views.IOModuleListAPI.as_view(), name="io"),
    path("", include(router.urls))
]
