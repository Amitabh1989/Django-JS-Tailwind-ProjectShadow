from django.urls import path, include
# from .views import UserRegistrationViewSet, UserAuthViewSet
from .views import UserRegistrationViewSet, UserLoginAPIView, UserProfileAPIView, UserChangePasswordAPIView,\
      SendResetPasswordEmailAPIView, ValidateResetPasswordEmailAPIView, UserLogoutAPIView
from rest_framework.routers import DefaultRouter

# app_name = "users"

router = DefaultRouter()


router.register(r"users", UserRegistrationViewSet, basename="userapi")
# router.register(r"login", UserAuthViewSet, basename="login")
# router.register(r"profile", UserAuthViewSet, basename="login")

urlpatterns = [
    path("", include(router.urls)), # UserRegistrationViewSet
    # path("register/", UserRegistrationViewSet.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("change_password/", UserChangePasswordAPIView.as_view(), name="change_password"),
    path('send-reset-password-email/', SendResetPasswordEmailAPIView.as_view(), name='send-reset-password-email'),
    path('reset_password/<uid>/<token>/', ValidateResetPasswordEmailAPIView.as_view(), name='reset_password'),
]

# router.register("", UserRegistrationViewSet, basename="userapi")
# router.register("login", UserAuthAPIView.as_view({"post": "create"}), basename="login")

# urlpatterns = [
#     path("", include(router.urls)),
#     path("/login/", UserAuthAPIView.as_view(), name="login")
# ]
