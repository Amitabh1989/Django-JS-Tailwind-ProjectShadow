from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from myapp.views import ConfigView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", TemplateView.as_view(template_name="testcase/tchome.html"), name="home"),
    path("admin/", admin.site.urls),
    path("io_module/", include("io_module.urls")),
    path("api/", include("api.urls"), name='api'),
    path("auth/", include("users.urls"), name='users'),
    path("restapi/", include('rest_framework.urls'), name="rest_framework"), # UserRegistrationViewSet
    path("config/", include("config.urls"), name='config')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()


# path("", TemplateView.as_view(template_name="index.html"), name="home"),
    # path("", TemplateView.as_view(template_name="index.html"), name="home"),
    
    # path("myapp/", include("myapp.urls")),
    # path("myapp/", ConfigView.as_view(), name="config_api_view"),
    # path("testcase/", include("testcase.urls")),