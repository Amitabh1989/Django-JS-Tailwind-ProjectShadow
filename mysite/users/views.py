from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import views
from .models import User
from django.contrib.auth import authenticate
from .serializers import UserModelSerializer, UserLoginAuthSerializer, UserProfileSerializer, UserChangePasswordSerializer, \
    SendResetPasswordEmailSerializer, ValidateResetPasswordSerializer
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from mysite.settings import PASSWORD_RESET_TIMEOUT
from rest_framework import renderers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model, login, logout
# Create your views here.


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [UserRenderer, renderers.BrowsableAPIRenderer]
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'users/login.html'
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        print(f"Entered the User Create function : {request.__dict__}")
        print(f"Entered the User Create function : {request.data}")
        print(f"Request accepted renderer        : {request.accepted_renderer}")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("User data is valid, saving the user now")
            user = serializer.save()
            token = get_tokens_for_user(user)
            context = {"msg": "User Registration successful!", "token": token}
            return Response(context, status=status.HTTP_201_CREATED)
        context = {"msg": "Bad user data", "error": serializer.errors, "non_field_errors": serializer.errors}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # return User.objects.all()
            return self.queryset
        else:
            # If the user is not an admin, we return an empty queryset.
            return self.queryset.none()

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
    authentication_classes = [authentication.SessionAuthentication] #, JWTAuthentication]
    # authentication_classes = [authentication.SessionAuthentication]
    # authentication_classes = [authentication.BasicAuthentication]
    
    def post(self, request, *args, **kwargs):
        print(f"Authview data received: {request.data}")
        serializer = UserLoginAuthSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as error:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            token = get_tokens_for_user(user)
            print(f"User ({user.name}) is authenticated")
            login(request, user)
            return Response({"msg": f"User ({user.name}) is authenticated", "token": token}, status=status.HTTP_200_OK)

        return Response({"msg": "User not found or invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        print(f"Entered the User List function : {request}")
        print(f"User list queryset : {self.queryset}")
        serializer = self.serializer_class(self.queryset, many=True)
        print(f"Serialized Data : {serializer}")        
        return Response({"msg": "User List Fetched successfully!", "response": serializer.data})

    def retrieve(self, request, *args, **kwargs):
        print("Hit the Retrieve Login url")
        return Response(template_name=self.template_name)

    
    def get(self, request, *args, **kwargs):
        # Check if the request accepts HTML, and if so, render the template
        if request.accepted_renderer.format == "html":
            return Response(template_name=self.template_name)
        # If the request doesn't accept HTML, return the response as usual
        return super().get(request, *args, **kwargs)

class UserProfileAPIView(views.APIView):
    renderer_classes = [UserRenderer, renderers.BrowsableAPIRenderer]
    permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [authentication.SessionAuthentication]

    def get(self, request, format=None):
        print(f"In Profile get : {request}")
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"msg": "User is logged out"}, status=status.HTTP_200_OK)



















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
