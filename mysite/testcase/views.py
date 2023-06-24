from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import TestStep, TestCase
import time
# Create your views here.

class TestCaseView(View):
    template_name = 'testcase/success.html'
    def post(self, request, *args, **kwargs):
        steps = request.POST.getlist('moduleForm')
        cqid = request.POST.get("cqid")
        title = "Dummy_TC_"
        summary = "Testing Model"
        tcid = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary)

        for step in steps:
            print("Saving step : {}".format(step))
            TestStep.objects.create(step=step)
        return HttpResponse("Data Submitted successfully!")
