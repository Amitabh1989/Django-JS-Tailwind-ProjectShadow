from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView,
    DeleteView, TemplateView, View)
from .models import ConfigModel
from .forms import ConfigModelForm

# from crispy_forms.helper import FormHelper
# from crispy_forms.mixin import CrispyFormMixin

# Create your views here.


# class ConfigView(CrispyFormMixin, CreateView):
class ConfigView(CreateView):
    model = ConfigModel
    form_class = ConfigModelForm
    template_name = "myapp/config.html"
    success_url = reverse_lazy("myapp:success")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        print(f"Cleaned data : {form.cleaned_data}")
        self.object = form.save()
        return super().form_valid(form)
    

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context["success_url"] = self.success_url


