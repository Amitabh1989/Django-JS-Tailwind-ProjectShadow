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
from mysite.modules import get_module_view_name, save_module_step
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from django.urls import reverse
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework import status
import time
import uuid
from itertools import chain
from copy import deepcopy

# Create your views here.


# class ConfigCreateAPIView(viewsets.ModelViewSet):
#     queryset = ConfigModel.objects.all()
#     serializer_class = ConfigModelSerializer

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
# class TestStepStats(viewsets.ModelViewSet):
#     """
#     TODO : Add user query in the steps. User can select to see stats with his selected
#     parameter as well. The request will be added to GET request and decoded here.
#     If no user query, will default to module type only
#     """
#     queryset = TestStep.objects.all()
#     serializer_class = TestStepSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [SessionAuthentication]
#     renderer_classes = [BrowsableAPIRenderer] #, TemplateHTMLRenderer]

#     # def get(self, request, *args, **kwargs):
#     def list(self, request, *args, **kwargs):
#         print("Request dict: {}".format(request.__dict__))
#         print("Request for stats from API: {}".format(request.GET))
#         print("Self.Request for stats : {}".format(self.request.GET))
#         print("Self.Request for body : {}".format(self.request.data))
#         request_data = self.request.GET
#         step = {key: value for key, value in request_data.items()}
#         print("Step is : {}".format(step))

#         response = {
#             "pk": False,
#             "fetched": False,
#             "exact_step": {},
#             "total_step_by_params": 0,  # How many test steps has same parameters as in MODULE_SEARCH_KEYMAP
#             "num_tc_associated": 0, 
#         }

#         print("Fetching Test Step Stats : step {}".format(step))
#         pk = False
#         fetched = False
#         total_step_by_params = 0
#         num_tc_associated = 0

#         # Contruct the user_query here:        
#         user_query = Q()
#         for field_name in MODULE_SEARCH_KEYMAP[step["module_type"]]:
#             print(f"Field name api/views : {field_name}")
#             if field_name == "module_type":
#                 continue
#             user_query &= Q(**{f'step__{field_name}': step[field_name]})
#         print("Filter params user_query : {}".format(user_query))

#         try:
#             test_step = TestStep.objects.filter(user_query)  # Test steps with primary MODULE_SEARCH_KEYMAP field
#             total_step_by_params = len(test_step)

#             exact_step = test_step.get(step=step)
#             print("Exact step GET : {}".format(exact_step))
#             print("Exact step GET TEST CASES: {}".format(exact_step.test_cases.all()))
#             for test_case in exact_step.test_cases.all():
#                 print("Test Case Title: {}".format(test_case.title))
#                 print("Test Case Summary: {}".format(test_case.summary))

#             # exact_step = test_step.filter(step=step)
#             exact_step = self.queryset.filter(step=step)
#             print("Exact step : {}".format(exact_step))
            
#             # num_tcs = exact_step.first().test_cases.all().count()   # Use the related name
#             num_tcs = TestCase.objects.filter(test_steps_list__in=exact_step)   # Use the related name
#             serialized_numTCs = TestCaseSerializer(instance=num_tcs, many=True)
#             print(f"Serialized numTcs : {serialized_numTCs}")
#             fetched = exact_step.exists()
#             if fetched:
#                 pk = getattr(exact_step.first(), 'pk', None)
#                 num_tc_associated = exact_step.first()
#             else:
#                 pk = False
#             print("Test Cases             : {}".format(total_step_by_params))
#             print("Test step              : {}".format(test_step))
#             print("Exact Test step        : {}".format(exact_step))
#             print("Exact Test num_tcs     : {}".format(num_tcs))
#             print("Exact num_tc_associate : {}".format(num_tc_associated))

#         except Exception as e:
#             print("Exception is : {}".format(e))
#             test_step = None
#         print("Test step fetched PK : {}".format(pk))

#         # serialized_test_step = TestStepSerializer(exact_step, many=True) # if fetched else {}
#         serialized_test_step = self.serializer_class(exact_step, many=True) # if fetched else {}
#         print("Serialized Test Step : {}".format(serialized_test_step))
#         print("Serialized Test Step : {}".format(serialized_test_step.data))
        
#         # num_tcs_serial = serialize('json', list(num_tcs)) if fetched else {}
#         # print("Num TCS : {}".format(num_tcs_serial))
#         # print("Num TCS JOSN : {}".format(num_tcs_serial))
#         response = {
#             "pk": pk,
#             "fetched": fetched,
#             "exact_step": serialized_test_step.data if serialized_test_step.data is not None else {},
#             "total_step_by_params": total_step_by_params,
#             # "tc_by_params": serialize('json', list(test_step)),
#             "tc_by_params": self.serializer_class(test_step).data,
#             "num_tc_associated": serialized_numTCs.data
#         }
#         print("Response is : {}".format(response))
#         return JsonResponse(response)
#         # return Response(response, status=status.HTTP_200_OK)


#     # def create(self, request, *args, **kwargs):
#     #     step_data = request.POST
#     #     step_list = [json.loads(step) for step in step_data]
#     #     print(f"Step List : {step_list}")
#     #     cqid = 2
#     #     title = "Dummy_TC_5"
#     #     summary = "Testing Model"
#     #     test_case, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary, user=request.user)
#     #     print("Created : {}".format(created))
        
#     #     # Create and associate TestStep instances with the TestCase
#     #     # test_step, _ = TestStep.objects.get_or_create(step=step)
#     #     for step in step_list[0]["moduleForm"]:
#     #         url = get_module_view_name_url(get_module_view_name(step["module_type"]))
#     #         data_request(url, step)
#     #         del step["csrfmiddlewaretoken"]
#     #         test_step, created = TestStep.objects.get_or_create(step=step, user=request.user) #, defaults={'step': step})
#     #         print(f"Value of Created is : {created}")
#     #         test_step.test_cases.set([test_case])
#     #         test_case.test_steps_list.add(test_step)
#     #         test_step.save()
#     #     test_case.save()
#     #     response = {"resp": "Submit successful from testcase view"}
#     #     test_steps = test_case.test_steps_list.all()
#     #     for test_step in test_steps:
#     #         print(test_step.step)
#     #     return JsonResponse(response)

#     def create(self, request, *args, **kwargs):
#         step_data = request.POST
#         step_list = [json.loads(step) for step in step_data]
#         print(f"Step List : {step_list}")
#         cqid = 2
#         title = "Dummy_TC_3"
#         summary = "Testing Model"
#         test_case, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary, user=request.user)
#         print("Created : {}".format(created))
#         print("test_case : {}".format(test_case))
        
#         # Create and associate TestStep instances with the TestCase
#         for step in step_list[0]["moduleForm"]:
#             view_name = get_module_view_name(step["module_type"])
#             url = reverse(view_name)
#             print(f"URL is : {url}")
#             save_module_step(url, step)
#             del step["csrfmiddlewaretoken"]
#             test_step, created = TestStep.objects.get_or_create(step=step, user=request.user) #, defaults={'step': step})
#             print(f"Value of Created is : {created}")
#             test_step.test_cases.add(test_case)
#             test_case.test_steps_list.add(test_step)
#             test_step.save()
#         test_case.save()
#         response = {"resp": "Submit successful from testcase view"}
#         test_steps = test_case.test_steps_list.all()
#         for test_step in test_steps:
#             print(test_step.step)
#         return JsonResponse(response)
        


class TestStepStats(viewsets.ModelViewSet):
    """
    TODO : Add user query in the steps. User can select to see stats with his selected
    parameter as well. The request will be added to GET request and decoded here.
    If no user query, will default to module type only
    """
    queryset = TestStep.objects.all()
    serializer_class = TestStepSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    renderer_classes = [BrowsableAPIRenderer] #, TemplateHTMLRenderer]

    # def get(self, request, *args, **kwargs):
    def list(self, request, *args, **kwargs):
        print("Request dict: {}".format(request.__dict__))
        print("Request for stats from API: {}".format(request.GET))
        print("Self.Request for stats : {}".format(self.request.GET))
        print("Self.Request for body : {}".format(self.request.data))
        request_data = self.request.GET
        step = {key: value for key, value in request_data.items()}
        print("Step is : {}".format(step))
        print("Fetching Test Step Stats : step {}".format(step))

        # Contruct the user_query here:
        # Here 2 things are happening,
        # 1. Get exact test step match
        # 2. Get Similar test steps  
        similar_step_query = Q()
        exact_step_query = Q()
        
        for field_name in step.keys():
            print(f"Field name api/views : {field_name}")
            if field_name == "module_type":
                continue
            if field_name in MODULE_SEARCH_KEYMAP[step["module_type"]]:
                similar_step_query &= Q(**{f'step__{field_name}': step[field_name]})
            exact_step_query &= Q(**{f'step__{field_name}': step[field_name]})

        print("Filter params user_query : {}".format(exact_step_query))
        print("Filter params user_query : {}".format(similar_step_query))

        ########################################################
        # Get EXACT TEST STEP details from Test Step Model
        ########################################################
        exact_test_step = self.queryset.filter(exact_step_query)
        print(f"Exact Step Details : {exact_test_step}")

        # Get Test Cases Associated with this Step
        testCases_with_exact_step = [test_step.test_cases.all() for test_step in exact_test_step]
        print(f"Exact Step Test Cases List : {testCases_with_exact_step}")

        combined_testCases_with_exact_step = list(chain(*testCases_with_exact_step))
        print(f"Exact Step Test Cases List Combined: {combined_testCases_with_exact_step}")

        # Get the test case details to create a hyperlink
        exact_step_testCase_details = [[tc.id, tc.cqid] for tc in combined_testCases_with_exact_step]
        print(f"Exact Step Test Cases ID List : {exact_step_testCase_details}")

        # Total Number of times this step has been used
        print(f"Total number times test step is used : {len(exact_test_step)}")


        ########################################################
        # Get SIMILAR TEST STEPS details from Test Step Model
        ########################################################
        similar_test_step = self.queryset.filter(similar_step_query)
        print(f"Similar Step Details : {similar_test_step}")

        # Get Test Cases Associated with this Step
        testCases_with_similar_step = [test_step.test_cases.all() for test_step in similar_test_step]
        print(f"Similar Step Test Cases Details : {testCases_with_similar_step}")

        combined_testCases_with_similar_step = list(set(chain(*testCases_with_similar_step)))
        print(f"Similar Step Test Cases List Combined: {combined_testCases_with_similar_step}")

        # Remove exact match from here
        if combined_testCases_with_similar_step:
            combined_testCases_with_similar_step = [tc for tc in combined_testCases_with_similar_step if 
                                                    tc not in combined_testCases_with_exact_step]
        print(f"Similar Step Test Cases Details trimmed : {combined_testCases_with_similar_step}")

        # Get the test case details to create a hyperlink
        serialized_exact_test_step = self.serializer_class(exact_test_step, many=True)
        serialized_similar_test_step = self.serializer_class(combined_testCases_with_similar_step, many=True)

        similar_test_step_tc_ids = [step.test_cases.all() for step in similar_test_step]

        print("Serialized Exact Test Step   : {}".format(serialized_exact_test_step.data))
        print("Serialized Similar Test Step : {}".format(serialized_similar_test_step.data))
        print("Similar Test Step Test Cases : {}".format(similar_test_step_tc_ids))
        
        exactStep_testCases = TestCaseSerializer(combined_testCases_with_exact_step, many=True).data
        similarStep_testCases = TestCaseSerializer(combined_testCases_with_similar_step, many=True).data
        keys_to_remove = []

        for d in exactStep_testCases:
            for i, k in d.items():
                if i == "test_steps_list":
                    keys_to_remove.append(i)

        for key in keys_to_remove:
            for d in exactStep_testCases:
                d.pop(key, None)

        print(exactStep_testCases)

        for d in similarStep_testCases:
            for i, k in d.items():
                if i == "test_steps_list":
                    keys_to_remove.append(i)
                    
        for key in keys_to_remove:
            for d in similarStep_testCases:
                d.pop(key, None)

        response = {
            "search_key": MODULE_SEARCH_KEYMAP[step["module_type"]], # What keys were looed for in the query
            "exact_test_step": serialized_exact_test_step.data,
            "similar_test_step": serialized_similar_test_step.data,
            "exactStep_testCases": exactStep_testCases,
            "similarStep_testCases": similarStep_testCases,
        }
        print("Response is : {}".format(response))
        return JsonResponse(response)
        # return Response(response, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        step_data = request.POST
        step_list = [json.loads(step) for step in step_data]
        print(f"Step List : {step_list}")
        # Generate a random UUID
        generated_uuid = uuid.uuid4()

        # Convert the UUID to a string
        user = request.user
        print(f"API create user is : {user}")
        uuid_string = str(generated_uuid)
        cqid = f"CQ_ID_{uuid_string}"
        title = f"Dummy_TC_{uuid_string[2:6]}"
        summary = "Testing Model"
        test_case, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary, user=request.user)
        print("Created : {}".format(created))
        print("test_case : {}".format(test_case))
        
        # Create and associate TestStep instances with the TestCase
        for step in step_list[0]["moduleForm"]:
            print(f"Sending step to save: {step}")
            view_name = get_module_view_name(step["module_type"])
            url = reverse(view_name)
            print(f"URL is : {url}")
            # save_module_step(url, step, user=request.user)
            save_module_step(url, step, request)
            del step["csrfmiddlewaretoken"]
            test_step, created = TestStep.objects.get_or_create(step=step, user=request.user) #, defaults={'step': step})
            print(f"Value of Created is : {created}")
            test_step.test_cases.add(test_case)
            test_case.test_steps_list.add(test_step)
            test_step.save()
            print("------------- Saved step, going for next\n\n\n")
        test_case.save()
        response = {"resp": "Submit successful from testcase view"}
        test_steps = test_case.test_steps_list.all()
        for test_step in test_steps:
            print(test_step.step)
        return JsonResponse(response)
