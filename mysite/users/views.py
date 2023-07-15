from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import views
from .models import User
from django.contrib.auth import authenticate
from .serializers import UserModelSerializer, UserLoginAuthSerializer, UserProfileSerializer, UserResetPasswordSerializer
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
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
    renderer_classes = [UserRenderer]

    def create(self, request, *args, **kwargs):
        print(f"Entered the User Create function : {request.__dict__}")
        print(f"Entered the User Create function : {request.data}")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("User data is valid, saving the user now")
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"msg": "User Registration successful!", "token": token}, status=status.HTTP_201_CREATED)
        return Response({"msg": "Bad user data", "error": serializer.errors, "non_field_errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        print(f"Entered the User List function : {request}")
        print(f"User list queryset : {self.queryset}")
        serializer = self.serializer_class(self.queryset, many=True)
        print(f"Serialized Data : {serializer}")        
        return Response({"msg": "User List Fetched successfully!", "response": serializer.data})
    

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


class UserLoginAPIView(views.APIView):
    renderer_classes = [UserRenderer]
    
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
            return Response({"msg": f"User ({user.name}) is authenticated", "token": token}, status=status.HTTP_200_OK)

        return Response({"msg": "User not found or invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileAPIView(views.APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(f"In Profile get : {request}")
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ResetPasswordAPIView(views.APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        print(f"In Profile get : {request}")
        serializer = UserResetPasswordSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)