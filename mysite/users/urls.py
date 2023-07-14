from django.urls import path, include

# from myapp.views import ConfigView

urlpatterns = [
    path("api/users", include("api.urls"), name='users')
]