from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import views
from .models import User, UserProfile
from django.contrib.auth import authenticate
from .serializers import UserModelSerializer, UserLoginAuthSerializer, UserProfileSerializer, UserChangePasswordSerializer, \
    SendResetPasswordEmailSerializer, ValidateResetPasswordSerializer
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from mysite.settings import PASSWORD_RESET_TIMEOUT
from rest_framework import renderers
from rest_framework.renderers import TemplateHTMLRenderer 
# from rest_framework.renderers import TemplateResponseRenderer
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, UserForm
# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationViewSet(viewsets.ModelViewSet):
    print(f'In user registrationviewset')
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # renderer_classes = [UserRenderer, renderers.BrowsableAPIRenderer]
    renderer_classes = [UserRenderer, TemplateHTMLRenderer, renderers.BrowsableAPIRenderer, ]
    # renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/register.html'
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'users/login.html'
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        print(f"Entered the User Create function : {request.__dict__}")
        print(f"Entered the User Create function : {request.POST}")
        # print(f"Request accepted renderer        : {request.accepted_renderer}")
        """
        => If the request's content type is application/json, request.data will be
           a dictionary containing the parsed JSON data.
        => If the request's content type is application/x-www-form-urlencoded
           (e.g., from HTML form submissions), request.data will be a dictionary
           containing the form data (equivalent to request.POST.dict()).
        => For other content types, like file uploads, request.data will contain
           the parsed data specific to the content type.
        """
        # Check if the request content type is JSON
        if 'application/json' in request.content_type:
            data_to_serialize = request.data
        else:
            # Assume it's form data (application/x-www-form-urlencoded)
            data_to_serialize = request.POST.dict()

        print(f"Data to serialize = {data_to_serialize}")
        serializer = self.serializer_class(data=data_to_serialize)
        try:
            serializer.is_valid(raise_exception=True)
            print("User data is valid, saving the user now")
            user = serializer.save()
            token = get_tokens_for_user(user)
            context = {"msg": "User Registration successful!", "token": token}
            return Response(context, status=status.HTTP_201_CREATED)
        
        except ValidationError as e:
            print(f"Exception is : {e}")
            error_msg = e
            if hasattr(e, "detail"):
                error_msg = e.detail
        context = {"msg": "Bad user data", "error": serializer.errors, "non_field_errors": serializer.errors}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    # def finalize_response(self, request, response, *args, **kwargs):
    #     print("Finalize response being called")
    #     # Set the appropriate renderer based on the request content type
    #     if 'application/json' in request.content_type:
    #         response.accepted_renderer = renderers.BrowsableAPIRenderer()
    #     else:
    #         response.accepted_renderer = TemplateHTMLRenderer()
    #     print(f"Finalize response being returned : {response.accepted_renderer}")
    #     return super().finalize_response(request, response, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # return User.objects.all()
            return self.queryset
        else:
            # If the user is not an admin, we return an empty queryset.
            return self.queryset.none()

    def list(self, request, *args, **kwargs):
        print(f"REgisterview LIST invoked : {request.GET}")
        if request.GET.get("pk"):
            pass
        # if request.accepted_renderer.format == "html":
            
        print("REgisterview LSIIT invoked")
        # Define your context data here
        if request.content_type == 'application/x-www-form-urlencoded':
            context = {"title": "User Registration Page"}
            form = UserForm()
            context["form"] = form
            print("Rendering user registration form")
            # return Response(context, template_name=self.template_name)
            return render(request, template_name=self.template_name, context=context)

        # Handle other formats (e.g., JSON) with the standard retrieve method
        return super().retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("REgisterview RETRIEVE invoked : here")
        if request.accepted_renderer.format == "html":
            print("REgisterview RETRIEVE invoked")
            # Define your context data here
            context = {"title": "User Registration Page"}
            form = UserForm()
            context["form"] = form
            # return Response(context, template_name=self.template_name)
            return render(request, template_name=self.template_name, context=context)

        # Handle other formats (e.g., JSON) with the standard retrieve method
        return super().retrieve(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     print("REgisterview GET invoked")
    #     # Check if the request accepts HTML, and if so, render the template
    #     if request.accepted_renderer.format == "html":
    #         context = {"message": "Hello, this is a message!"}
    #         return Response(context, template_name=self.template_name)
    #         # return render(request, self.template_name, context)
    #     # If the request doesn't accept HTML, return the response as usual
    #     return super().get(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     print(f"Entered the User List function : {request}")
    #     print(f"User list queryset : {self.queryset}")
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     print(f"Serialized Data : {serializer}")        
    #     return Response({"msg": "User List Fetched successfully!", "response": serializer.data})



class UserLoginAPIView(views.APIView):
    renderer_classes = [UserRenderer, TemplateHTMLRenderer, renderers.BrowsableAPIRenderer]
    template_name = 'users/login.html'
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]
    # authentication_classes = [authentication.SessionAuthentication] #, JWTAuthentication]
    # authentication_classes = [authentication.SessionAuthentication]
    # authentication_classes = [authentication.BasicAuthentication]
    
    def post(self, request, *args, **kwargs):
        print(f"Authview data received: {request.data}")
        print(f"Authview data received POST REQ : {request.POST.dict()}")

        # Check if the request content type is JSON
        if 'application/json' in request.content_type:
            data_to_serialize = request.data
        else:
            # Assume it's form data (application/x-www-form-urlencoded)
            data_to_serialize = request.POST.dict()


        serializer = UserLoginAuthSerializer(data=data_to_serialize)
        print(f"Serializer data : {serializer}")
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as error:
            print(f"Serializer errors : {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user = authenticate(request, email=email, password=password)
        print(f"User authenticated : {user}")

        if user:
            token = get_tokens_for_user(user)
            print(f"User ({user.name}) is authenticated")
            login(request, user)
            if not 'application/json' in request.content_type:
                return HttpResponseRedirect(reverse("users:profile") + f"?user_id={user.id}")
            
            return Response({"msg": f"User ({user.name}) is authenticated", "token": token}, status=status.HTTP_200_OK)
        return Response({"msg": "User not found or invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
        print(f"Entered the User List function : {request}")
        print(f"User list queryset : {self.queryset}")
        serializer = self.serializer_class(self.queryset, many=True)
        print(f"Serialized Data : {serializer}")        
        return Response({"msg": "User List Fetched successfully!", "response": serializer.data})
    
    # def finalize_response(self, request, response, *args, **kwargs):
    #     print("Finalize response being called")
    #     # Set the appropriate renderer based on the request content type
    #     if 'application/json' in request.content_type:
    #         response.accepted_renderer = renderers.BrowsableAPIRenderer()
    #     else:
    #         response.accepted_renderer = TemplateHTMLRenderer()
    #     print(f"Finalize response being returned : {response.accepted_renderer}")
    #     return super().finalize_response(request, response, *args, **kwargs)
    
    # def retrieve(self, request, *args, **kwargs):
    #     print("Hit the Retrieve Login url")
    #     return Response(template_name=self.template_name)

    
    def get(self, request, *args, **kwargs):
        # Check if the request accepts HTML, and if so, render the template
        print("In login GET function")
        if request.accepted_renderer.format == "html":
            return Response(template_name=self.template_name)
        # If the request doesn't accept HTML, return the response as usual
        return super().get(request, *args, **kwargs)

class UserProfileAPIView(views.APIView):
    renderer_classes = [UserRenderer, TemplateHTMLRenderer, renderers.BrowsableAPIRenderer]
    permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    template_name = "users/profile.html"
    authentication_classes = [SessionAuthentication]
    # permission_classes = [authentication.SessionAuthentication]

    def get(self, request, format=None):
        print(f"In Profile get : {request.__dict__}")
        serializer = UserProfileSerializer(request.user)

        # if request.content_type == 'application/x-www-form-urlencoded':
        print(f"I am here in user profile html rendered view : serialized data {serializer}")
        profile_data = serializer.data
        context = {}
        # Accessing the associated UserProfile object for the current User
        try:
            user_profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            user_profile = None  # Handle the case where UserProfile doesn't exist for the user

        context = {
            "profile": user_profile,
            "serializer": profile_data,
        }

        return render(request, self.template_name, context)
        # return HttpResponseRedirect(self.template_name)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get("user_id")
        print("Getting user context")
        if user_id:
            user = User.objects.get(pk=user_id)
            profile = user.profile
            context["profile1"] = profile
            print(f"Returing User profile: {context}")
        return context
    

class UserChangePasswordAPIView(views.APIView):
    renderer_classes = [UserRenderer, renderers.BrowsableAPIRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        print(f"In Profile get : {request}")
        serializer = UserChangePasswordSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.update(request.user, serializer.validated_data)
            return Response({"msg": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendResetPasswordEmailAPIView(views.APIView):
    renderer_classes = [UserRenderer, renderers.BrowsableAPIRenderer]
    
    def post(self, request, *args, **kwargs):
        serializer = SendResetPasswordEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"msg": f"Reset email sent. Its valid for {PASSWORD_RESET_TIMEOUT} minsutes only"})

class ValidateResetPasswordEmailAPIView(views.APIView):
    renderer_classes = [UserRenderer, renderers.BrowsableAPIRenderer]

    def post(self, request, uid, token, *args, **kwargs):
        serializer = ValidateResetPasswordSerializer(data=request.data,
                                                          context={"uid": uid, "token": token})
        serializer.is_valid(raise_exception=True)
        print(f"Srialized data {serializer.data}")
        user = serializer.validated_data["user"]
        serializer.update(user, serializer.validated_data)
        return Response({"msg": "Password has been updated. Try login with new password"})

class UserLogoutAPIView(views.APIView):
    print("Logout class called")
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        print(f"Logout Request : {request.__dict__}")
        logout(request)
        return Response({"msg": "User is logged out"}, status=status.HTTP_200_OK)
    
    # def dispatch(self, request, *args, **kwargs):
    #     print(f"Request for logout: {request.__dict__}")
    #     request.method = "POST"
    #     return super().dispatch(request, *args, **kwargs)



















# class UserAuthAPIView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         print(f"Authview data received : {request.data}")
#         serializer = UserAuthSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             email = serializer.data.get("email")
#             password = serializer.data.get("password")
#             user = authenticate(email, password)
#             if user:
#                 print("User authenticated")
#                 return Response({"errors": {"non_field_errors": ["Email or Password is invalid"]}}, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserAuthViewSet(viewsets.ViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserAuthSerializer
#     renderer_classes = [UserRenderer]

#     def create(self, request, *args, **kwargs):
#         print(f"Authview data received : {request.data}")
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(): # If we raise_exception here, else part does not execute
#             email = serializer.data.get("email")
#             password = serializer.data.get("password")
#             user = authenticate(email=email, password=password)
#             if user:
#                 print("User authenticated")
#                 return Response({"msg": f"User ({user.name}) is authenticated"}, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get_exception_handler(self):
    #     """
    #     Override the exception handler to include renderer classes for serializer errors.
    #     """
    #     renderer_classes = getattr(self, 'renderer_classes', [])
    #     return lambda exc, context: self.handle_exception(exc, context, renderer_classes)

# class UserAuthViewSet(viewsets.ViewSet):
#     queryset = User.objects.all()
#     # serializer_class = UserLoginAuthSerializer
#     renderer_classes = [UserRenderer]

#     def get_serializer_class(self):
#         if self.action == 'create':
#             self.serializer_class = UserLoginAuthSerializer
#             return UserLoginAuthSerializer
#         elif self.action == 'list':
#             self.serializer_class = UserProfileSerializer
#             return UserProfileSerializer
#         return super().get_serializer_class()

#     def create(self, request, *args, **kwargs):
#         print(f"Authview data received: {request.data}")
#         serializer = self.serializer_class(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as error:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         email = serializer.validated_data.get("email")
#         password = serializer.validated_data.get("password")
#         user = authenticate(request, email=email, password=password)

#         if user:
#             token = get_tokens_for_user(user)
#             print(f"User ({user.name}) is authenticated")
#             return Response({"msg": f"User ({user.name}) is authenticated", "token": token}, status=status.HTTP_200_OK)

#         return Response({"msg": "User not found or invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request, pk=None, *args, **kwargs):
#         print(f"In get request : {request.GET}")
#         if pk:
#             user = self.queryset.get(pk=pk)
#             print(f"User got : {user}")
#             serializer = self.serializer_class(user, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 return Response({"msg": "User profile is valid"}, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
