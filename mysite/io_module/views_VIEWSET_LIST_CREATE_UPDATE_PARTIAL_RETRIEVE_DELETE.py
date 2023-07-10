from .models import IOModule
from rest_framework import viewsets
from .serializers import IOModuleSerializer
from rest_framework.response import Response
from rest_framework import status

class IOModuleViewSet(viewsets.ViewSet):
    def list(self, request):
        print("***** LIST VIEWSET *****")
        print(f"BASENAME : {self.basename}")
        print(f"ACTION   : {self.action}")
        print(f"DETAIL   : {self.detail}")
        print(f"SUFFIX   : {self.suffix}")
        print(f"NAME     : {self.name}")
        print(f"DSESCRIP : {self.description}")
        model = IOModule.objects.all()
        serializer = IOModuleSerializer(model, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        print("***** RETRIEVE VIEWSET *****")
        print(f"BASENAME : {self.basename}")
        print(f"ACTION   : {self.action}")
        print(f"DETAIL   : {self.detail}")
        print(f"SUFFIX   : {self.suffix}")
        print(f"NAME     : {self.name}")
        print(f"DSESCRIP : {self.description}")
        if pk is not None:
            model = IOModule.objects.get(pk=pk)
            serializer = IOModuleSerializer(model)
            return Response(serializer.data)
    
    def update(self, request, pk=None):
        print("***** UPDATE VIEWSET *****")
        print(f"BASENAME : {self.basename}")
        print(f"ACTION   : {self.action}")
        print(f"DETAIL   : {self.detail}")
        print(f"SUFFIX   : {self.suffix}")
        print(f"NAME     : {self.name}")
        print(f"DSESCRIP : {self.description}")
        model = IOModule.objects.get(pk=pk)
        serializer = IOModuleSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        print("***** PARTIAL UPDATE VIEWSET *****")
        print(f"BASENAME : {self.basename}")
        print(f"ACTION   : {self.action}")
        print(f"DETAIL   : {self.detail}")
        print(f"SUFFIX   : {self.suffix}")
        print(f"NAME     : {self.name}")
        print(f"DSESCRIP : {self.description}")
        model = IOModule.objects.get(pk=pk)
        serializer = IOModuleSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
        print("***** CREATE VIEWSET *****")
        print(f"BASENAME : {self.basename}")
        print(f"ACTION   : {self.action}")
        print(f"DETAIL   : {self.detail}")
        print(f"SUFFIX   : {self.suffix}")
        print(f"NAME     : {self.name}")
        print(f"DSESCRIP : {self.description}")
        serializer = IOModuleSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data created"}) #, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        print("***** DELETE VIEWSET *****")
        print(f"BASENAME : {self.basename}")
        print(f"ACTION   : {self.action}")
        print(f"DETAIL   : {self.detail}")
        print(f"SUFFIX   : {self.suffix}")
        print(f"NAME     : {self.name}")
        print(f"DSESCRIP : {self.description}")
        model = IOModule.objects.get(pk=pk)
        model.delete()
        return Response({"msg": "Data Deleted"})
    