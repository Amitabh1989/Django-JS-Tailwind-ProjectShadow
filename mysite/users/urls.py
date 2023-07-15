from django.urls import path, include
from .views import UserRegistrationViewSet, UserAuthViewSet
from rest_framework.routers import DefaultRouter

# app_name = "users"

router = DefaultRouter()


router.register(r"users", UserRegistrationViewSet, basename="userapi")
router.register(r"login", UserAuthViewSet, basename="login")
# router.register(r"profile", UserAuthViewSet, basename="login")

urlpatterns = [
    path("", include(router.urls)),
    # path("login/", UserAuthViewSet.as_view({"post": "create"}), name="login")
]

# router.register("", UserRegistrationViewSet, basename="userapi")
# router.register("login", UserAuthAPIView.as_view({"post": "create"}), basename="login")

# urlpatterns = [
#     path("", include(router.urls)),
#     path("/login/", UserAuthAPIView.as_view(), name="login")
# ]
