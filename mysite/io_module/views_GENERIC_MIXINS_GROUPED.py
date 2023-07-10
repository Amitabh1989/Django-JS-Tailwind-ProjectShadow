from .models import IOModule
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .serializers import IOModuleSerializer


class LCIOModuleAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request=request, *args, **kwargs)

class RUDIOModuleAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = IOModule.objects.all()
    serializer_class = IOModuleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request=request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request=request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request=request, *args, **kwargs)