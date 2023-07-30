from django.urls import path, include
from django.views.generic import TemplateView
from .views import TestCaseView, TestStepDetail, TestStepStats, TestCaseListRestAPI
from rest_framework.routers import DefaultRouter

app_name = "testcase"

router = DefaultRouter()
router.register("tcs", TestCaseListRestAPI, basename="tcs") # list of test cases

urlpatterns = [
    path("", include(router.urls)),
]


# router.register("api", TestStepStats, basename="teststep")
