from .models import IOModule
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .serializers import IOModuleSerializer


class IOModuleList(GenericAPIView, ListModelMixin):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

class IOModuleCreate(GenericAPIView, CreateModelMixin):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request=request, *args, **kwargs)

class IOModuleRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request=request, *args, **kwargs)

class IOModuleUpdate(GenericAPIView, UpdateModelMixin):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request=request, *args, **kwargs)

class IOModuleDestroy(GenericAPIView, DestroyModelMixin):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request=request, *args, **kwargs)