from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
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
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class ConfigViewSetAPI(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    renderer_classes = [renderers.JSONRenderer, BrowsableAPIRenderer] 
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.SessionAuthentication]
    # Override the renderers attribute to enforce JSON rendering
    # renderer_classes = [renderers.JSONRenderer]
    # renderer_classes = [TemplateHTMLRenderer]
    print("Config View set API called")

    def dispatch(self, request, *args, **kwargs):
        # user = request.META.get("HTTP_AUTHORIZATION", "").replace("Bearer ", "")
        print(f"Config dispatch : request : {request.POST}")
        print(f"Config dispatch : request.user : {request.user}")
        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print(f"Config create : User Authenticated : {self.request.user.is_authenticated}")
        print("This is POST request from CONFIG view")
        print("Request _data is : {}".format(self.request.data))
        _data =  dict(self.request.data)
        user = self.request.user
        _data = {key: value[0] if isinstance(value, list) else value for key, value in _data.items()}
        partial_update_data = {}
        query = Q()
        # del _data['csrfmiddlewaretoken']
        for field, value in _data.items():
            print(f"Field name : {field}  Value : {value}")
            if field in ("module_type", "csrfmiddlewaretoken"):
                continue
            query &= Q(**{f'{field}': value})
        print(f"Query is : {query}")

        obj = self.queryset.filter(query).filter(user=self.request.user).first()
        print(f"OBJ : {obj}")

        if obj:
            print(f"Obj {obj} already exists, not creating again : {obj.pk}")
            print(f"Obj {obj} use count : {obj._use_count}")
            # Update the record with +1 use count
            instance = obj
            # instance._use_count += 1
            instance.save()
            print(f"Instance is : {instance}")
            print(f"Instance use count : {instance._use_count}")
            return Response({"msg": "Partial update done"})
        print("After partial update, proceeding")
        _data["user"] = user.id 
        serializer = self.serializer_class(data=_data)
        if serializer.is_valid(raise_exception=True):
            print(f"Config serialized data : {serializer.validated_data}")
            print(f"Config serialized errors : {serializer.errors}")
            serializer.save()
            return Response({"msg": "New config submitted"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, data=None, pk=None, **kwargs):
        print("partial_update from config.views is invoked")
        model = self.queryset.get(pk=pk)
        # model = self.get_object()
        print(f"Model is : {model}")
        print(f"PK is    : {pk}")
        print(f"Data is  : {data}")

        serializer = self.serializer_class(model, data=data, partial=True)
        print(f"Config partial update serialized is : {serializer}")
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print("Partial update done")
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, pk=None, **kwargs):
        # return super().partial_update(request, *args, **kwargs)
        print("List view config.views is invoked")

        model = self.queryset.all()
        serializer = self.serializer_class(model, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        # return super().partial_update(request, *args, **kwargs)
        print("Retrieve view config.views is invoked")
        
        # model = self.queryset.get(pk=pk)
        model = self.get_object()
        print(f"Model is : {model}")
        print(f"PK is    : {pk}")
        serializer = self.serializer_class(model)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConfigModelCreateView(CreateView):
    model = ConfigModel
    template_name = "testcase/input_form.html"
    form_class = ConfigModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["module_name"] = self.model.module_type.field.get_default()
        print(f"CONFIG I am here in this view already! Context {context}")
        return context