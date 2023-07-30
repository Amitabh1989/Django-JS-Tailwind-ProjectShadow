from .models import TestCase, TestStep
from rest_framework import serializers

class TestCaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'