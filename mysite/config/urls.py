from django.urls import path, include
from rest_framework.routers import DefaultRouter
from config import views

app_name = "config"

router = DefaultRouter()

router.register("api", views.ConfigViewSetAPI, basename="config")

urlpatterns = [
    path("", include(router.urls)),
    path("form/", views.ConfigModelCreateView.as_view(), name="config_form")
]
