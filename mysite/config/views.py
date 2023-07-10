from django.shortcuts import render
from rest_framework import viewsets
from .models import ConfigModel
from .serializers import ConfigModelSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
import json
# Create your views here.

class ConfigViewSetAPI(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer

    def create(self, request, *args, **kwargs):
        # data =  dict(request.POST)
        # data =  json.loads(request.body.decode('utf-8'))
        print("This is POST request")
        print("Request data is : {}".format(self.request.POST))
        print("Request data is : {}".format(self.request.data))
        data =  dict(self.request.data)
        data = {key: value[0] for key, value in data.items()}
        
        query = Q()
        data["vdcount"] = int(data["vdcount"])
        data["pdcount"] = int(data["pdcount"])
        data["spans"] = int(data["spans"])
        data["stripe"] = int(data["stripe"])
        data["dtabcount"] = int(data["dtabcount"])
        data["hotspare"] = int(data["hotspare"])
        data["repeat"] = int(data["repeat"])
        print(f"Data is : {data}")
        del data['csrfmiddlewaretoken']
        print(f"Data is : {data}")

        for field_name in data:
            query &= Q(**{f'{field_name}': self.request.data[field_name]})
        print("Query is : {}".format(query))
        
        obj = self.queryset.filter(query)

        if obj.exists():
            print(f"Obj {obj} already exists, not creating again")
            return Response({"msg": "Obj already exists"}, status=status.HTTP_201_CREATED)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "New config submitted"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)