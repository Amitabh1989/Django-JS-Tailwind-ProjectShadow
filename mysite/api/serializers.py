from rest_framework import serializers
from config.models import ConfigModel
from testcase.models import TestCase, TestStep


class TestStepSerializer(serializers.ModelSerializer):
    # test_case = TestCaseSerializer(many=True, read_only=True, source='test_cases')  # Use the related_name as source
    test_cases = serializers.SlugRelatedField(slug_field='cqid', many=True, read_only=True)

    class Meta:
        model = TestStep
        # fields = '__all__'
        fields = ['id', 'test_cases', 'step', 'created_on', 'updated_on']
    
    def create(self, validated_data):
        return super().create(validated_data)

class TestCaseSerializer(serializers.ModelSerializer):
    test_steps_list = TestStepSerializer(many=True)
    class Meta:
        model = TestCase
        # fields = '__all__'
        fields = ["id", "cqid", "title", "summary", "test_steps_list", "created_on", "updated_on"]

class ConfigModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigModel
        fields = '__all__'
        