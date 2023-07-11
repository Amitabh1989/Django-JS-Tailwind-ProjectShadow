from django.urls import path, include
from io_module import views
from rest_framework.routers import DefaultRouter

app_name = 'io'

router = DefaultRouter()

router.register("api", views.IOModelModelViewSet, basename="io")

urlpatterns = [
    path("", include(router.urls)),
    path("form/", views.IOModelCreateView.as_view(), name="io_form"),
]
