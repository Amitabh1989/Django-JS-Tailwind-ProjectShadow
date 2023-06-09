from django.urls import path
from django.views.generic import TemplateView

app_name = "test_case"

urlpatterns = [
    path("", TemplateView.as_view(template_name="testcase/tchome.html"), name="tchome")
]
