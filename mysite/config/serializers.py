from rest_framework import serializers
from config.models import ConfigModel

class ConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigModel
        # fields = '__all__'
        # read_only_fields = ["module_type", "user"]
        exclude = ["module_type", "_use_count"]