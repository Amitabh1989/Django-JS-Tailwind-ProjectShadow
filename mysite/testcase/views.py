from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import View, DeleteView, UpdateView, ListView, DetailView
from .models import TestStep, TestCase
import time, json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import Q, Value

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
            del step["csrfmiddlewaretoken"]
            test_step, _ = TestStep.objects.get_or_create(step=step)
            test_step.test_cases.set([tcid])
            tcid.test_steps_list.add(test_step)
        response = {"resp": "Submit successful from testcase view"}
        test_steps = tcid.test_steps_list.all()
        for test_step in test_steps:
            print(test_step.step)
        return JsonResponse(response)

class TestStepStats(View):
    def get(self, request, *args, **kwargs):
        print("Request for stats : {}".format(request.GET))
        print("Self.Request for stats : {}".format(self.request.GET))
        request_data = self.request.GET
        print("Self.Request num_pds : {}".format(self.request.GET["num_pds"]))
        step = {
            "num_pds": request_data.get("num_pds", "2"),
            "num_vds": request_data.get("num_vds", "2"),
            "raid": request_data.get("raid", "R0"),
            "size": request_data.get("size", "12")
        }
        response = {
            "fetched": False,
            "step_stats": {},  # this has been changed from data
            "pk": False,
            "total_raid_hits": 0,
            "num_tc_associated": 0, 
        }
        print("Fetching Test Step Stats : step {}".format(step))
        fetched = False
        total_raid_hits = 0
        pk = False
        num_tc_associated = 0
        try:
            # test_step = TestStep.objects.filter(step=step).first()
            # all = TestStep.objects.all()
            # test_step = TestStep.objects.filter(step=Value(step)
            """
            # Assuming you have a queryset named `queryset`
            first_instance = queryset.first()  # Get the first model instance from the queryset
            pk = getattr(first_instance, 'pk', None)  # Retrieve the primary key (pk) attribute

            # You can also directly access the `pk` attribute
            pk = first_instance.pk

            # If you want to retrieve the primary keys of all instances in the queryset
            pks = queryset.values_list('pk', flat=True)  # Returns a list of primary keys            
            """
            test_step = TestStep.objects.filter(Q(step__raid=step["raid"]))
            total_raid_hits = len(test_step)
            exact_step = test_step.filter(Q(step__num_pds=step["num_pds"]) & Q(step__num_vds=step["num_vds"]) & Q(step__size=step["size"]))
            # num_tcs = exact_step.first().test_cases.all().count()   # Use the related name
            num_tcs = TestCase.objects.filter(test_steps_list__in=exact_step)   # Use the related name
            fetched = exact_step.exists()
            if fetched:
                pk = getattr(exact_step.first(), 'pk', None)
                num_tc_associated = exact_step.first()
            else:
                pk = False
            print("Test Cases : {}".format(total_raid_hits))
            print("Test step : {}".format(test_step))
            print("Exact Test step : {}".format(exact_step))
            print("Exact Test num_tcs : {}".format(num_tcs))
            print("Exact Test step num_tc_associate : {}".format(num_tc_associated))
        # except (TestStep.DoesNotExist, AttributeError):
        except Exception as e:
            print("Exception is : {}".format(e))
            test_step = None
        print("Test step fetched PK : {}".format(pk))
        # Extract testcases details if fetched
        # test_case_details = self.get_test_case_details(test_step)

        serialized_test_step = serialize('json', list(exact_step)) if fetched else {}
        num_tcs_serial = serialize('json', list(num_tcs)) if fetched else {}
        response = {
            "fetched": fetched,
            "data": serialized_test_step,
            "pk": pk,
            "total_raid_hits": total_raid_hits,
            "num_tc_associated": num_tcs_serial
        }
        print("Response is : {}".format(response))
        return JsonResponse(response)


    # def get_test_case_details(self, test_step):
    #     return test_step.test
    
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
        print("Test Step Details : {}".format(teststep_detail))
        print("All TC Step Details : {}".format(teststep_detail.test_cases.all()))
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
        print("Data being sent : {}".format(data))
        return JsonResponse(data, **response_kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['teststep_detail_list'] = TestStep.objects.all()  # Replace this with your desired queryset
    #     print("Context data is : {}".format(context))
    #     return context

