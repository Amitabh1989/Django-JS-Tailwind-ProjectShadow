from .models import IOModule
from .serializers import IOModuleSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
class IOModuleListCreateAPI(ListCreateAPIView):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

class IOModuleRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer
