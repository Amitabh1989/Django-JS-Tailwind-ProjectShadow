from .models import TestCase, TestStep
from rest_framework import serializers

class TestStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStep
        fields = ["step"]  # Include the fields you want to display


class TestCaseListSerializer(serializers.ModelSerializer):
    test_steps_list = TestStepSerializer(many=True)
    class Meta:
        model = TestCase
        fields = ["cqid", "title", "summary", "test_steps_list"]