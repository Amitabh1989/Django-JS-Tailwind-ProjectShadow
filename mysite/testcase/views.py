from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import View, DeleteView, UpdateView, ListView, DetailView
from .models import TestStep, TestCase
import time, json
from django.http import JsonResponse

# Create your views here.

class TestCaseView(View):
    template_name = 'testcase/success.html'
    def post(self, request, *args, **kwargs):
        body = request.body.decode('utf-8')
        data = json.loads(body)
        steps = data["moduleForm"]
        print("Steps received is : {}".format(steps))
        cqid = 1
        title = "Dummy_TC_2"
        summary = "Testing Model"
        tcid, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary)
        print("Created : {}".format(created))

        # Create and associate TestStep instances with the TestCase
        for step in steps:
            test_step, _ = TestStep.objects.get_or_create(step=step)
            tcid.test_steps_list.add(test_step)
        response = {"resp": "Submit successful from testcase view"}
        test_steps = tcid.test_steps_list.all()
        for test_step in test_steps:
            print(test_step.step)
        return JsonResponse(response)

class TestCaseList(ListView):
    model = TestCase
    queryset = TestCase.objects.order_by('updated_on')


class TestStepDetail(DetailView):
    model = TestStep
    context_object_name = "teststep_detail"
    # queryset = TestStep.objects.prefetch_related('test_cases').order_by('updated_on')
    queryset = TestStep.objects.prefetch_related('test_cases').all()
    print("Returning QuerySet : {}".format(queryset))

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.select_related('test_cases')
    #     print("Queryset : {}".format(queryset) )
    #     return super().get_queryset()

