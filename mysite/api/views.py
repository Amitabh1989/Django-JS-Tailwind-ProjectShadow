from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from config.models import ConfigModel
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q, Value
from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
import json
# Create your views here.


class ConfigCreateAPIView(generics.CreateAPIView):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigModelSerializer

    # def form_valid(self, form):
    #     print(f"Cleaned data : {form.cleaned_data}")
    #     self.object = form.save()
    #     return super().form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     print("In dispatch : {}".format(request.META))
    #     if request.META.get('QUERY_STRING', False):
    #         q_str = request.META.get("QUERY_STRING").split('&')
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
class TestStepStats(APIView):
    def get(self, request, *args, **kwargs):
        print("Request for stats from API: {}".format(request.GET))
        print("Self.Request for stats : {}".format(self.request.GET))
        print("Self.Request for body : {}".format(self.request.data))
        request_data = self.request.GET
        # print("Self.Request num_pds : {}".format(self.request.GET["pdcount"]))

        step = {key: value for key, value in request_data.items()}
        print("Step is : {}".format(step))
        response = {
            "pk": False,
            "fetched": False,
            "step_stats": {},  # this has been changed from data
            "total_raid_hits": 0,
            "num_tc_associated": 0, 
        }
        print("Fetching Test Step Stats : step {}".format(step))
        pk = False
        fetched = False
        total_raid_hits = 0
        num_tc_associated = 0

        # Contruct the query here:
        
        query = Q()
        for field_name in MODULE_SEARCH_KEYMAP[step["module_type"]]:
            query &= Q(**{f'step__{field_name}': step[field_name]})

        # filter_params = {}
        # for field_name in MODULE_SEARCH_KEYMAP[step["module_type"]]:
        #     filter_params[f'step__{field_name}'] = step[field_name]
        print("Filter params : {}".format(query))
        try:
            # test_step = TestStep.objects.filter(Q(step__raid=step["raid"]))
            # test_step = TestStep.objects.filter(Q(step__raid=MODULE_SEARCH_KEYMAP[step["module_type"]]))
            # test_step = TestStep.objects.filter(**filter_params)
            test_step = TestStep.objects.filter(query)
            total_raid_hits = len(test_step)
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
            print("Test Cases             : {}".format(total_raid_hits))
            print("Test step              : {}".format(test_step))
            print("Exact Test step        : {}".format(exact_step))
            print("Exact Test num_tcs     : {}".format(num_tcs))
            print("Exact num_tc_associate : {}".format(num_tc_associated))

        except Exception as e:
            print("Exception is : {}".format(e))
            test_step = None
        print("Test step fetched PK : {}".format(pk))

        serialized_test_step = TestStepSerializer(exact_step, many=True) # if fetched else {}
        print("Serialized Test Step : {}".format(serialized_test_step))
        print("Serialized Test Step : {}".format(serialized_test_step.data))
        
        num_tcs_serial = serialize('json', list(num_tcs)) if fetched else {}
        print("NUm TCS : {}".format(num_tcs_serial))
        print("NUm TCS JOSN : {}".format(json.loads(num_tcs_serial)))
        response = {
            "pk": pk,
            "fetched": fetched,
            "data": serialized_test_step.data if serialized_test_step.data is not None else {},
            "total_raid_hits": total_raid_hits,
            "num_tc_associated": json.loads(num_tcs_serial)
        }
        print("Response is : {}".format(response))
        return JsonResponse(response)