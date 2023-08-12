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
# from myapp.models import ConfigModel
from io_module.models import IOModel
from api.serializers import TestCaseSerializer, TestStepSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TestCaseListSerializer
from rest_framework import status
from .renderers import TCRenderer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class TestCaseView(View):
    template_name = '/testcase/success.html'
    def post(self, request, *args, **kwargs):
        body = request.body.decode('utf-8')
        data = json.loads(body)
        steps = data["moduleForm"]
        print("Steps received is : {}".format(steps))
        cqid = 1
        title = "Dummy_TC_3"
        summary = "Testing Model"
        tcid, created = TestCase.objects.get_or_create(cqid=cqid, title=title, summary=summary)
        print("Created : {}".format(created))

        # Create and associate TestStep instances with the TestCase
        for step in steps:
            del step["csrfmiddlewaretoken"]
            test_step, _ = TestStep.objects.get_or_create(step=step)
            test_step.test_cases.set([tcid])
            tcid.test_steps_list.add(test_step)
            test_step.save()
        tcid.save()
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
        step = {k: v[0] for k, v in request_data}
        print(f"Step data is : {step}")

        query = Q()
        for key, value in step.items():
            query &= Q(**{f'step__{key}': value})
        print(f"Query is : {query}")
        response = {
            "pk": False,
            "fetched": False,
            "step_stats": {},
            "total_step_by_params": 0,
            "num_tc_associated": 0, 
        }
        print("Fetching Test Step Stats : step {}".format(step))
        pk = False
        fetched = False
        total_step_by_params = 0
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
            total_step_by_params = len(test_step)

            exact_step = test_step.filter( 
                step__pdcount=step["pdcount"],
                step__vdcount=step["vdcount"],
                step__size=step["size"],
                step__spans=step["spans"],
                step__stripe=step["stripe"],
                step__dtabcount=step["dtabcount"],
                step__hotspare=step["hotspare"],
                step__init=step["init"],
                step__readpolicy=step["readpolicy"],
                step__writepolicy=step["writepolicy"],
                step__repeat=step["repeat"]
            )
            print("Exact step : {}".format(exact_step))
            # num_tcs = exact_step.first().test_cases.all().count()   # Use the related name
            num_tcs = TestCase.objects.filter(test_steps_list__in=exact_step)   # Use the related name
            fetched = exact_step.exists()
            if fetched:
                pk = getattr(exact_step.first(), 'pk', None)
                num_tc_associated = exact_step.first()
            else:
                pk = False
            print("Test Cases : {}".format(total_step_by_params))
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

        # serialized_test_step = serialize('json', list(exact_step)) if fetched else {}
        serialized_test_step = TestStepSerializer(exact_step, many=True) # if fetched else {}
        print("Serialized Test Step : {}".format(serialized_test_step))
        # print("Serialized Test Step : {}".format(serialized_test_step.data))
        
        num_tcs_serial = serialize('json', list(num_tcs)) if fetched else {}
        response = {
            "fetched": fetched,
            "data": serialized_test_step.data if serialized_test_step.data is not None else {},
            # "data": serialized_test_step,
            "pk": pk,
            "total_step_by_params": total_step_by_params,
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

class TestCaseListRestAPI(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    renderer_classes = [TCRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TestCaseListSerializer
    template_name = "testcase/tclist.html"

    def list(self, request, *args, **kwargs):
        print(f"Request : {request.__dict__}")
        accepted_media_type = request.accepted_media_type
        print(f"Accepted media type : {accepted_media_type}")
        paginator = Paginator(self.queryset, 25) # Show 25 contacts per page
        user = request.user
        tc_list = self.queryset.filter(user=user)
        serializer = self.serializer_class(instance=tc_list, many=True)
        print(f"TC List User is : {user}")
        print(f"TC list is      : {tc_list}")
        print(f"Serializer is   : {serializer}")
        print(f"Serializer data : {serializer.data}")
        try:
            data = paginator.page(serializer.data)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            data = paginator.page(paginator.num_pages)

        # serializer.is_valid(raise_exception=True)
        # return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        if accepted_media_type == 'text/html':
            # return render(request, self.template_name, {"data": serializer.data})
            return render(request, self.template_name, {"data": data})
        # return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request, *args, **kwargs):
        print(f"Request retrieve : {request.__dict__}")
        user = request.user
        tc_instance = self.get_object()
        accepted_media_type = request.accepted_media_type
        serializer = self.serializer_class(instance=tc_instance, many=False)
        test_steps = tc_instance.test_steps_list.all()
        step_details = [test_step.step for test_step in test_steps]
        print(f"Test Steps of test case are : {test_steps}")
        print(f"Test Steps details are : {step_details}")
        print(f"User is : {user}")
        print(f"TC detail is : {tc_instance}")
        print(f"Serializer is : {serializer.data}")
        # serializer.is_valid(raise_exception=True)
        if accepted_media_type == 'text/html':
            print("Returning Retrieved data as text/html")
            # return render(request, self.template_name, {"detail": serializer.data})
            return render(request, "testcase/tcdetail.html", {"detail": serializer.data})
        print("Returning Retrieved data as serialized data")
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    # def get_renderer_context(self):
    #     # Check if the request is from the Browsable API (text/html)
    #     if self.request.accepted_renderer.format == 'html':
    #         return {'request': self.request._request, 'view': self}

    #     # For other requests (e.g., JSON, XML), use default behavior
    #     return super().get_renderer_context()