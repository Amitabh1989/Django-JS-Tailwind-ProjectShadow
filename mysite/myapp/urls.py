from django.urls import path
from .views import ConfigView, TestCaseView
from django.views.generic import TemplateView

app_name = "myapp"

urlpatterns = [
    path("", ConfigView.as_view(), name="config"),
    # path("success/", TemplateView.as_view(template_name="myapp/success.html"), name="success")
    path("success/", TestCaseView.as_view(), name="success")
]
