from rest_framework import serializers
from .models import ConfigModel

class ConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigModel
        fields = "__all__"