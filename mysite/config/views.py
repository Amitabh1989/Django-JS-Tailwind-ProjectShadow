from typing import Any, Dict
from django.shortcuts import render
from rest_framework import viewsets
from config.models import ConfigModel
from config.serializers import ConfigModelSerializer
from config.forms import ConfigModelForm
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
import json
from django.views.generic import CreateView
# Create your views here.

class ConfigViewSetAPI(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer
    # renderer_classes = [TemplateHTMLRenderer]
    print("Config View set API called")

    def create(self, request, *args, **kwargs):
        # _data =  dict(request.POST)
        # _data =  json.loads(request.body.decode('utf-8'))
        print("This is POST request")
        print("Request _data is : {}".format(self.request.data))
        _data =  dict(self.request.data)
        _data = {key: value[0] for key, value in _data.items()}
        
        query = Q()
        del _data['csrfmiddlewaretoken']
        for fields, value in _data.items():
            query &= Q(**{f'{fields}': value})
        print(f"Query is : {query}")

        obj = self.queryset.filter(query)
        print(f"OBJ : {obj}")

        if obj.exists():
            print(f"Obj {obj} already exists, not creating again")
            return Response({"msg": "Obj already exists"}, status=status.HTTP_201_CREATED)

        serializer = self.serializer_class(data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "New config submitted"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ConfigModelCreateView(CreateView):
    model = ConfigModel
    template_name = "config/input_form.html"
    form_class = ConfigModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["module_name"] = self.model.module_type.field.get_default()
        print(f"CONFIG I am here in this view already! Context {context}")
        return context