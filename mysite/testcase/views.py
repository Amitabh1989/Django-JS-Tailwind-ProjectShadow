from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import TestStep, TestCase
import time, json
from django.http import JsonResponse
# Create your views here.

# class TestCaseView(View):
#     template_name = 'testcase/success.html'
#     def post(self, request, *args, **kwargs):
#         # print("Steps received is : {}".format(request.__dict__))
#         # steps = request.POST.getlist('moduleForm')
#         body = request.body.decode('utf-8')
#         data = json.loads(body)
#         steps = data["moduleForm"]
#         print("Steps received is : {}".format(steps))
#         # cqid = request.POST.get("cqid")
#         cqid = 1
#         title = "Dummy_TC_"
#         summary = "Testing Model"
#         tcid, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary)
#         print("Created : {}".format(created))
#         for step in steps:
#             print("Saving step : {}".format(step))
#             j = TestStep.objects.create(step=step, test_case=tcid)
#             j.save()
#         response = {"resp": "Submit successful from testcase view"}
#         test_steps = tcid.test_steps.all()
#         for test_step in test_steps:
#             print(test_step.step)
#         return JsonResponse(response)


class TestCaseView(View):
    template_name = 'testcase/success.html'
    def post(self, request, *args, **kwargs):
        # print("Steps received is : {}".format(request.__dict__))
        # steps = request.POST.getlist('moduleForm')
        body = request.body.decode('utf-8')
        data = json.loads(body)
        steps = data["moduleForm"]
        print("Steps received is : {}".format(steps))
        # cqid = request.POST.get("cqid")
        cqid = 1
        title = "Dummy_TC_"
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
