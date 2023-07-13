from django.urls import path, include
from django.views.generic import TemplateView
from .views import TestCaseView, TestStepDetail, TestStepStats
from rest_framework.routers import DefaultRouter

app_name = "testcase"

router = DefaultRouter()
router.register("api", TestStepStats, baename="teststep")

urlpatterns = [
    path("", include('routers.urls'))
]


# urlpatterns = [
#     path("", TemplateView.as_view(template_name="testcase/tchome.html"), name="tchome"),
#     # path("success/", TemplateView.as_view(template_name="testcase/success.html"), name="tc_success"),
#     path("success/", TestCaseView.as_view(), name="success"),
#     path("teststep_detail/<int:pk>/", TestStepDetail.as_view(), name="teststep_detail"),
#     path("teststep_stats/", TestStepStats.as_view(), name="teststep_stats"),

# ]