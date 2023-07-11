from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.http.response import HttpResponseBase
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView,
    DeleteView, TemplateView, View)
from config.models import ConfigModel
from .forms import ConfigModelForm
from django.http import JsonResponse
from api.views import ConfigCreateAPIView

# from crispy_forms.helper import FormHelper
# from crispy_forms.mixin import CrispyFormMixin

# Create your views here.


# class ConfigView(CrispyFormMixin, CreateView):
# class ConfigView(CreateView):
#     model = ConfigModel
#     form_class = ConfigModelForm
#     template_name = "myapp/config.html"
#     success_url = reverse_lazy("myapp:success")

#     def form_valid(self, form: BaseModelForm) -> HttpResponse:
#         print(f"Cleaned data : {form.cleaned_data}")
#         self.object = form.save()
#         return super().form_valid(form)

#     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
#         print("In dispatch : {}".format(request.META))
#         if request.META.get('QUERY_STRING', False):
#             q_str = request.META.get("QUERY_STRING").split('&')
#             if q_str[0].split("=")[1] == "True":
#                 # print("Context data : {}".format(self.get_context_data()))
#                 form = self.get_form()
#                 # print("Form is : {}".format(form))
#                 request.META["form"] = form
#                 return self.ajax_get(request, *args, **kwargs)
#         return super().dispatch(request, *args, **kwargs)

#     def ajax_get(self, request, *args, **kwargs):
#         print("Got the ajax request")
#         # context_data = {"key1": [1, 2, 3]}
#         return JsonResponse({"form": request.META["form"].as_table()})

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['module_name'] = self.model.module_type.field.get_default()
#         return context

class ConfigView(CreateView):
    model = ConfigModel
    form_class = ConfigModelForm
    template_name = "myapp/config.html"
    success_url = reverse_lazy("myapp:success")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        print(f"Cleaned data : {form.cleaned_data}")
        self.object = form.save()
        return super().form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        print("In dispatch : {}".format(request.META))
        if request.META.get('QUERY_STRING', False):
            q_str = request.META.get("QUERY_STRING").split('&')
            if q_str[0].split("=")[1] == "True":
                # print("Context data : {}".format(self.get_context_data()))
                form = self.get_form()
                # print("Form is : {}".format(form))
                request.META["form"] = form
                return self.ajax_get(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def ajax_get(self, request, *args, **kwargs):
        print("Got the ajax request")
        # context_data = {"key1": [1, 2, 3]}
        return JsonResponse({"form": request.META["form"].as_table()})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['module_name'] = self.model.module_type.field.get_default()
        return context
