from typing import Any, Dict
from rest_framework import viewsets
from .serializers import IOModelSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer, BrowsableAPIRenderer, JSONRenderer
from django.views.generic import CreateView
from .forms import IOModelForm
from .models import IOModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class IOModelModelViewSet(viewsets.ModelViewSet):
    queryset = IOModel.objects.all()
    serializer_class = IOModelSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer] 
    # renderer_classes = [TemplateHTMLRenderer]

    def create(self, request, *args, **kwargs):
        print("This is POST request")
        # print("Request data is : {}".format(self.request.POST.dict()))
        print("Request data is : {}".format(self.request.data))
        print(f"IO create : User Authenticated : {self.request.user.is_authenticated}")
        print(f"IO create : User : {self.request.user}")
        user = self.request.user
        # data = dict(self.request.data)
        # data = {key: value[0] for key, value in data.items()}
        _data = self.request.data.dict()
        print("Request data is : {}".format(_data))
        query = Q()
        for fields, value in _data.items():
            if fields == "csrfmiddlewaretoken":
                continue
            query &= Q(**{f'{fields}': value})
        print(f"Query is : {query}")

        obj = self.queryset.filter(query).filter(user=self.request.user).first()
        print(f"IO obj is : {obj}")

        _data["user"] = user.id 

        if obj:
            obj._use_count += 1
            data = {"_use_count": obj._use_count}
            print(f"Obj.pk : {obj.pk}")
            print(f"Use count : {obj._use_count}")
            obj.save()
            # self.partial_update(request, pk=obj.pk, data=data, user=self.request.user)
            # self.partial_update(request, pk=obj.pk, data=data)
            return Response({"msg": "Obj already present"}, status=status.HTTP_201_CREATED)
        
        serialilzer = self.serializer_class(data=_data)
        serialilzer.is_valid(raise_exception=True)
        serialilzer.save()
        return Response({"msg": "Obj created"}, status=status.HTTP_201_CREATED)
        # print(f"Serializer errors : {serialilzer.errors}")
        # return Response(serialilzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, data=None, *args, **kwargs):
        print(f"Request received here: {request}")
        obj = self.queryset.get(pk=pk, user=self.request.user)
        # obj = self.get_object()
        print("IO partial update user is : {}".format(obj))
        serializer = self.serializer_class(data=data, instance=obj, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Use count increased"})

    # @action(detail=False, methods=['get'])
    # def form(self, request):
    #     serializer = self.get_serializer()
    #     return render(request, 'io_module/io.html', {'form': serializer})

    # def retrieve(self, request, *args, **kwargs):
    #     # return super().retrieve(request, *args, **kwargs)
    #     # return render(request, 'io_module/io.html', {'form': self.serializer_class})
    #     return Response({'serializer': self.serializer_class})


class IOModelCreateView(CreateView):
    print("I am here in this view already!")
    model = IOModel
    template_name = "testcase/input_form.html"
    form_class = IOModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["module_name"] = self.model.module_type.field.get_default()
        print(f"I am here in this view already! Context {context}")
        return context