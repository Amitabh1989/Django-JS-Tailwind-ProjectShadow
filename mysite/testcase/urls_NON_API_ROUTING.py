from django.urls import path
from django.views.generic import TemplateView
from .views import TestCaseView, TestStepDetail, TestStepStats

app_name = "testcase"

urlpatterns = [
    path("", TemplateView.as_view(template_name="testcase/tchome.html"), name="tchome"),
    # path("success/", TemplateView.as_view(template_name="testcase/success.html"), name="tc_success"),
    path("success/", TestCaseView.as_view(), name="success"),
    path("teststep_detail/<int:pk>/", TestStepDetail.as_view(), name="teststep_detail"),
    path("teststep_stats/", TestStepStats.as_view(), name="teststep_stats"),

]
