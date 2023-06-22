from django.urls import path
from django.views.generic import TemplateView

app_name = "test_case"

urlpatterns = [
    path("", TemplateView.as_view(template_name="testcase/tchome.html"), name="tchome"),
    path("success/", TemplateView.as_view(template_name="testcase/success.html"), name="tc_success"),
]
