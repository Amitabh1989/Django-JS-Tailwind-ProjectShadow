from .models import IOModule
from rest_framework import viewsets
from .serializers import IOModuleSerializer

class IOModuleModelViewSet(viewsets.ModelViewSet):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer