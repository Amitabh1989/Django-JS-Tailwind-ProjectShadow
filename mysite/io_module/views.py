from .models import IOModule
from rest_framework import viewsets
from .serializers import IOModuleSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status


class IOModuleModelViewSet(viewsets.ModelViewSet):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

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

        obj = self.queryset.filter(query)

        if obj.exists():
            return Response({"msg": "Obj already present"}, status=status.HTTP_201_CREATED)
        
        obj = obj.first()
        serialilzed = self.serializer_class(obj, data=data)
        if serialilzed.is_valid():
            serialilzed.save()
            return Response({"msg": "Obj created"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)