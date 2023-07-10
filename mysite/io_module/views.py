from django.shortcuts import render
from django.views.generic import CreateView
from .models import IOModule
from .forms import IOModuleForm
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import IOModuleSerializer
from rest_framework import status
from django.db.models import Q
# Create your views here.

class IOModuleView(APIView):
    model = IOModule
    form_class = IOModuleForm
    serializer_class = IOModuleSerializer
    template_name = "io_module/io.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module_name'] = self.model.module_type.field.get_default()
        return context

    def get(self, request, format=None, pk=None, *args, **kwargs):
        print("This is GET request")
        print("Request data is : {}".format(self.request.GET))
        data = self.request.data
        print("Data is : {}".format(data))
        id = pk
        print("ID is : {}".format(id))
        if id is None:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(id=id)
        print("Queryset is : {}".format(queryset))

        serializer = self.serializer_class(instance=queryset, many=True)
        
        # if serializer.is_valid():
        print("Serializer is valid : {}".format(serializer.data))
        return Response(serializer.data)
        # return Response({'errors': serializer.errors})

    def post(self, request, format=None, *args, **kwargs):
        print("This is POST request")
        print("Request data is : {}".format(self.request.POST))
        print("Request data is : {}".format(self.request.data))
        query = Q()
        for field_name in self.request.data:
            query &= Q(**{f'{field_name}': self.request.data[field_name]})
        
        print("Query is : {}".format(query))

        obj = self.model.objects.filter(query)
        # obj, created = self.model.objects.get_or_create(query)
        print("OBJ is : {}".format(obj))
        if obj.count == 0:
            serializer = IOModuleSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': "data has been saved"}, status= status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Data already available in DB"}, status=status.HTTP_302_FOUND)
    
    def put(self, request, format=None, pk=None,  *args, **kwargs):
        print("This is PUT request")
        print("Request data is : {}".format(self.request.GET))
        data = self.request.data
        print("Data is : {}".format(data))
        id = pk
        print("ID is : {}".format(id))
        if id is None:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(id=id)
        print("Queryset is : {}".format(queryset))

        serializer = self.serializer_class(instance=queryset, many=True)
        
        if serializer.is_valid():
            serializer.save()
            print("Serializer is valid : {}".format(serializer.data))
            return Response({"msg": "Data has been updated for ID {}".format(pk)}, serializer.data, status=status.HTTP_200_OK)
        return Response({"msg": "Data not updated for ID {}".format(pk)}, serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None, pk=None,  *args, **kwargs):
        print("This is PATCH request")
        print("Request data is : {}".format(self.request.GET))
        data = self.request.data
        print("Data is : {}".format(data))
        id = pk
        print("ID is : {}".format(id))
        queryset = self.model.objects.filter(id=id)
        print("Queryset is : {}".format(queryset))

        if queryset.exists():
            instance = queryset.first()
            serializer = self.serializer_class(instance=instance, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            print("Serializer is valid : {}".format(serializer.data))
            return Response({"msg": "Data has been updated for ID {}".format(pk)}, status=status.HTTP_200_OK)
        return Response({"msg": "Data not updated for ID {}".format(pk)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None, pk=None,  *args, **kwargs):
        print("This is PUT request")
        print("Request data is : {}".format(self.request.GET))
        data = self.request.data
        print("Data is : {}".format(data))
        id = pk
        print("ID is : {}".format(id))
        queryset = self.model.objects.filter(id=id)
        print("Queryset is : {}".format(queryset))
        if queryset.exists():
            queryset.delete()
            print("Record deleted for ID {}".format(id))
            return Response({"msg": "Data has been deleted for ID {}".format(pk)}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Data not deleted for ID {}".format(pk)}, status=status.HTTP_400_BAD_REQUEST)