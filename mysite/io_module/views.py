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
        data = dict(self.request.data)
        data = {key: value[0] for key, value in data.items()}
        del data['csrfmiddlewaretoken']
        query = Q()
        for fields, value in data.items():
            query &= Q(**{f'{fields}': value})
        print(f"Query is : {query}")

        obj = self.queryset.filter(query).first()

        if obj.exists():
            return Response({"msg": "Obj already present"}, status=status.HTTP_201_CREATED)
        
        serialilzed = self.serializer_class(data=data)
        if serialilzed.is_valid():
            serialilzed.save()
            return Response({"msg": "Obj created"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
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
    template_name = 'io_module/input_form.html'
    form_class = IOModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["module_name"] = self.model.module_type.field.get_default()
        print(f"I am here in this view already! Context {context}")
        return context