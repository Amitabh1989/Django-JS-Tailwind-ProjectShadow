from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from myapp.models import ConfigModel
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.


class ConfigCreateAPIView(generics.CreateAPIView):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer

    # def form_valid(self, form):
    #     print(f"Cleaned data : {form.cleaned_data}")
    #     self.object = form.save()
    #     return super().form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     print("In dispatch : {}".format(request.META))
    #     if request.META.get('QUERY_STRING', False):
    #         q_str = request.META.get("QUERY_STRING").split('&')
    #         if q_str[0].split("=")[1] == "True":
    #             # print("Context data : {}".format(self.get_context_data()))
    #             form = self.get_form()
    #             # print("Form is : {}".format(form))
    #             request.META["form"] = form
    #             return self.ajax_get(request, *args, **kwargs)
    #     return super().dispatch(request, *args, **kwargs)

    # def ajax_get(self, request, *args, **kwargs):
    #     print("Got the ajax request")
    #     # context_data = {"key1": [1, 2, 3]}
    #     return JsonResponse({"form": request.META["form"].as_table()})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['module_name'] = self.model.module_type.field.get_default()
    #     return context
