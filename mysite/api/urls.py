from django.urls import path, include
from .views import TestStepStats
from rest_framework.routers import DefaultRouter

app_name = "api"

# router = DefaultRouter()
# router.register(r'stepstat/', TestStepStats, basename='stepstat')


# urlpatterns = [
#     path('api', include(router.urls)),
# ]

urlpatterns = [
    path("stepstat/", TestStepStats.as_view(), name="stepstat")
]
