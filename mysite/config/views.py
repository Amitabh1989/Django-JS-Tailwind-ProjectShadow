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
from rest_framework import renderers
import json
from django.views.generic import CreateView
from rest_framework import permissions, authentication
# Create your views here.

class ConfigViewSetAPI(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    # Override the renderers attribute to enforce JSON rendering
    # renderer_classes = [renderers.JSONRenderer]
    # renderer_classes = [TemplateHTMLRenderer]
    print("Config View set API called")

    def create(self, request, *args, **kwargs):
        # _data =  dict(request.POST)
        # _data =  json.loads(request.body.decode('utf-8'))
        print("This is POST request")
        print("Request _data is : {}".format(self.request.data))
        _data =  dict(self.request.data)
        _data = {key: value[0] if isinstance(value, list) else value for key, value in _data.items()}
        
        query = Q()
        del _data['csrfmiddlewaretoken']
        for field, value in _data.items():
            print(f"Field name : {field}  Value : {value}")
            if field == "module_type":
                continue
            query &= Q(**{f'{field}': value})
        print(f"Query is : {query}")

        obj = self.queryset.filter(query)
        print(f"OBJ : {obj}")

        if obj.exists():
            print(f"Obj {obj.first()} already exists, not creating again : {obj.first().pk}")
            # Update the record with +1 use count
            data = {"_use_count": int(obj.first()._use_count+1)}
            resp = self.partial_update(request, data=data, pk=obj.first().pk)
            print(f"REsp seen is : {resp}")
            return Response({"msg": "Partial update done"})
            # return resp
            # return self.partial_update(request, data=data, pk=obj.first().pk)
        print("After partial update, proceeding")
        serializer = self.serializer_class(data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "New config submitted"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, data=None, pk=None, **kwargs):
        # return super().partial_update(request, *args, **kwargs)
        print("partial_update from config.views is invoked")
        model = self.queryset.get(pk=pk)
        print(f"Model is : {model}")
        print(f"PK is    : {pk}")
        print(f"Data is  : {data}")

        serializer = self.serializer_class(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfigModelCreateView(CreateView):
    model = ConfigModel
    template_name = "testcase/input_form.html"
    form_class = ConfigModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["module_name"] = self.model.module_type.field.get_default()
        print(f"CONFIG I am here in this view already! Context {context}")
        return context