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
        title = "Dummy_TC_0"
        summary = "Testing Model"
        tcid, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary)
        print("Created : {}".format(created))

        # Create and associate TestStep instances with the TestCase
        for step in steps:
            del step["csrfmiddlewaretoken"]
            test_step, _ = TestStep.objects.get_or_create(step=step)
            test_step.test_cases.set([tcid])
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
    """
    The default behavior of the `render_to_response` method in Django's `DetailView`
    is to render a template with the provided context and return an HTML response.
    By default, it uses the template specified in the `template_name` attribute
    of the view or follows the naming convention to determine the template name.

    When you override the `render_to_response` method in the example I provided,
    you are changing the default behavior to return a JSON response instead of
    rendering an HTML template. The overridden method constructs the JSON
    response by extracting the desired data from the context and serializing
    it into JSON using the `JsonResponse` class.

    It's important to note that the default behavior of `render_to_response`
    may vary depending on the specific class being used (e.g., `DetailView`,
    `ListView`, etc.) and can be further customized based on your requirements.
    """
    model = TestStep
    context_object_name = "teststep_detail"
    queryset = TestStep.objects.prefetch_related('test_cases').order_by('updated_on')
    print("Returning QuerySet : {}".format(queryset))

    def render_to_response(self, context, **response_kwargs):
        teststep_detail = context.get(self.context_object_name)
        data = {
            'step': teststep_detail.step,
            'test_cases': [
                {
                    'cqid': testcase.cqid,
                    'title': testcase.title,
                    'summary': testcase.summary,
                    "updated_on": testcase.updated_on
                }
                for testcase in teststep_detail.test_cases.all()
            ]
        }
        return JsonResponse(data, **response_kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['teststep_detail_list'] = TestStep.objects.all()  # Replace this with your desired queryset
    #     print("Context data is : {}".format(context))
    #     return context

