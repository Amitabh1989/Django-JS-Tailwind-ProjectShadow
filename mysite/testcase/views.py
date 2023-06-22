from django.shortcuts import render
from django.views.generic import View
from .models import TestStep
# Create your views here.

class TestCaseView(View):
    def post(self, request, *args, **kwargs):
        steps = request.POST.getlist('steps')
        for step in steps:
            TestStep.objects.create(step=step)
