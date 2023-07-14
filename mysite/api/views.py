from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from config.models import ConfigModel
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q, Value
from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework import viewsets
import json
from mysite.modules import Modules, data_request, get_module, get_url

# Create your views here.


class ConfigCreateAPIView(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer

    # def form_valid(self, form):
    #     print(f"Cleaned data : {form.cleaned_data}")
    #     self.object = form.save()
    #     return super().form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     print("In dispatch : {}".format(request.META))
    #     if request.META.get('user_query_STRING', False):
    #         q_str = request.META.get("user_query_STRING").split('&')
    #         if q_str[0].split("=")[1] == "True":
    #             # print("Context data : {}".format(self.get_context_data()))
    #             form = self.get_form()
    #             # print("Form is : {}".format(form))
    #             request.META["form"] = form
    #             return self.ajax_get(request, *args, **kwargs)
    #     return super().dispatch(request, *args, **kwargs)

    # def ajax_get(self, request, *args, **kwargs):
    #     print("Got the ajax request")
    #     # context_data = {"key1": [1, 2, 3]}
    #     return JsonResponse({"form": request.META["form"].as_table()})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['module_name'] = self.model.module_type.field.get_default()
    #     return context


MODULE_SEARCH_KEYMAP = {
    "config": ["raid"],
    "io": ["tool"]
}

# class TestStepStats(APIView):
class TestStepStats(viewsets.ModelViewSet):
    """
    TODO : Add user query in the steps. User can select to see stats with his selected
    parameter as well. The request will be added to GET request and decoded here.
    If no user query, will default to module type only
    """
    queryset = TestStep.objects.all()
    serializer_class = TestStepSerializer

    # def get(self, request, *args, **kwargs):
    def list(self, request, *args, **kwargs):
        print("Request for stats from API: {}".format(request.GET))
        print("Self.Request for stats : {}".format(self.request.GET))
        print("Self.Request for body : {}".format(self.request.data))
        request_data = self.request.GET
        step = {key: value for key, value in request_data.items()}
        print("Step is : {}".format(step))

        response = {
            "pk": False,
            "fetched": False,
            "exact_step": {},  # this has been changed from data
            "total_step_by_params": 0,
            "num_tc_associated": 0, 
        }

        print("Fetching Test Step Stats : step {}".format(step))
        pk = False
        fetched = False
        total_step_by_params = 0
        num_tc_associated = 0

        # Contruct the user_query here:        
        user_query = Q()
        for field_name in MODULE_SEARCH_KEYMAP[step["module_type"]]:
            print(f"Field name api/views : {field_name}")
            if field_name == "module_type":
                continue
            user_query &= Q(**{f'step__{field_name}': step[field_name]})
        print("Filter params : {}".format(user_query))

        try:
            test_step = TestStep.objects.filter(user_query)
            total_step_by_params = len(test_step)
            exact_step = test_step.filter(step=step)
            print("Exact step : {}".format(exact_step))
            
            # num_tcs = exact_step.first().test_cases.all().count()   # Use the related name
            num_tcs = TestCase.objects.filter(test_steps_list__in=exact_step)   # Use the related name
            fetched = exact_step.exists()
            if fetched:
                pk = getattr(exact_step.first(), 'pk', None)
                num_tc_associated = exact_step.first()
            else:
                pk = False
            print("Test Cases             : {}".format(total_step_by_params))
            print("Test step              : {}".format(test_step))
            print("Exact Test step        : {}".format(exact_step))
            print("Exact Test num_tcs     : {}".format(num_tcs))
            print("Exact num_tc_associate : {}".format(num_tc_associated))

        except Exception as e:
            print("Exception is : {}".format(e))
            test_step = None
        print("Test step fetched PK : {}".format(pk))

        # serialized_test_step = TestStepSerializer(exact_step, many=True) # if fetched else {}
        serialized_test_step = self.serializer_class(exact_step, many=True) # if fetched else {}
        print("Serialized Test Step : {}".format(serialized_test_step))
        print("Serialized Test Step : {}".format(serialized_test_step.data))
        
        num_tcs_serial = serialize('json', list(num_tcs)) if fetched else {}
        print("Num TCS : {}".format(num_tcs_serial))
        print("Num TCS JOSN : {}".format(num_tcs_serial))
        response = {
            "pk": pk,
            "fetched": fetched,
            "exact_step": serialized_test_step.data if serialized_test_step.data is not None else {},
            "total_step_by_params": total_step_by_params,
            "tc_by_params": serialize('json', list(test_step)),
            "num_tc_associated": num_tcs_serial
        }
        print("Response is : {}".format(response))
        return JsonResponse(response)


    def create(self, request, *args, **kwargs):
        step_data = request.POST
        step_list = [json.loads(step) for step in step_data]
        print(f"Step List : {step_list}")
        cqid = 2
        title = "Dummy_TC_5"
        summary = "Testing Model"
        tcid, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary)
        print("Created : {}".format(created))
        
        # Create and associate TestStep instances with the TestCase
        # test_step, _ = TestStep.objects.get_or_create(step=step)
        for step in step_list[0]["moduleForm"]:
            url = get_url(get_module(step["module_type"]))
            data_request(url, step)
            del step["csrfmiddlewaretoken"]
            test_step, created = TestStep.objects.get_or_create(step=step) #, defaults={'step': step})
            print(f"Value of Created is : {created}")
            test_step.test_cases.set([tcid])
            tcid.test_steps_list.add(test_step)
            test_step.save()
        tcid.save()
        response = {"resp": "Submit successful from testcase view"}
        test_steps = tcid.test_steps_list.all()
        for test_step in test_steps:
            print(test_step.step)
        return JsonResponse(response)

        
