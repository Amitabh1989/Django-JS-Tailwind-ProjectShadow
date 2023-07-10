from rest_framework import serializers
from .models import IOModule


class IOModuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IOModule
        fields = "__all__"
        read_only_fields = ["module_type"]