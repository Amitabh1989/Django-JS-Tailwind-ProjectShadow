from django.urls import path, include
from .views import TestStepStats
from rest_framework.routers import DefaultRouter
# from io_module.views import IOModuleView
from myapp.views import ConfigView
app_name = "api"

router = DefaultRouter()
# router.register(r'stepstat/', TestStepStats, basename='stepstat')
# router.register(r'io', IOModuleView, basename='io')

print("I am searching here. in API url.py. Is that correct?")

urlpatterns = [
    path('config/', ConfigView.as_view(), name='config'),
    # path('io/', IOModuleView.as_view(), name='io'),
    # path("stepstat/", TestStepStats.as_view(), name="stepstat")
    path("stepstat/", TestStepStats.as_view({"get": "list", "post": "create"}), name="stepstat"),
]
