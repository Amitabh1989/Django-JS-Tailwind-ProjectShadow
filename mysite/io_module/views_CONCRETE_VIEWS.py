from .models import IOModule
from .serializers import IOModuleSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView

class IOModuleCreateAPI(CreateAPIView):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer


class IOModuleUpdateAPI(UpdateAPIView):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer


class IOModuleRetrieveAPI(RetrieveAPIView):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer


class IOModuleDestroyAPI(DestroyAPIView):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

class IOModuleListAPI(ListAPIView):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer
