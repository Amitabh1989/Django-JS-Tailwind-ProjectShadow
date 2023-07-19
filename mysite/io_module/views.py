from typing import Any, Dict
from rest_framework import viewsets
from .serializers import IOModelSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic import CreateView
from .forms import IOModelForm
from .models import IOModel


class IOModelModelViewSet(viewsets.ModelViewSet):
    queryset = IOModel.objects.all()
    serializer_class = IOModelSerializer
    # renderer_classes = [TemplateHTMLRenderer]

    def create(self, request, *args, **kwargs):
        print("This is POST request")
        print("Request data is : {}".format(self.request.POST))
        print("Request data is : {}".format(self.request.data))
        # data = dict(self.request.data)
        # data = {key: value[0] for key, value in data.items()}
        del self.request.data['csrfmiddlewaretoken']
        query = Q()
        for fields, value in self.request.data.items():
            query &= Q(**{f'{fields}': value})
        print(f"Query is : {query}")

        obj = self.queryset.filter(query).first()

        if obj:
            data = {"_use_count": obj._use_count+1}
            print(f"Obj.pk : {obj.pk}")
            print(f"Use count : {obj._use_count}")
            self.partial_update(request, pk=obj.pk, data=data)
            return Response({"msg": "Obj already present"}, status=status.HTTP_201_CREATED)
        
        serialilzer = self.serializer_class(data=self.request.data)
        if serialilzer.is_valid(raise_exception=True):
            serialilzer.save()
            return Response({"msg": "Obj created"}, status=status.HTTP_201_CREATED)
        return Response(serialilzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, data=None, *args, **kwargs):
        print(f"Request received here: {request}")
        obj = self.queryset.get(pk=pk)
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