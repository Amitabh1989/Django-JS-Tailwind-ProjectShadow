"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from myapp.views import ConfigView

urlpatterns = [
    path("", TemplateView.as_view(template_name="testcase/tchome.html"), name="home"),
    # path("", TemplateView.as_view(template_name="index.html"), name="home"),
    # path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("admin/", admin.site.urls),
    path("myapp/", include("myapp.urls")),
    # path("myapp/", ConfigView.as_view(), name="config_api_view"),
    path("testcase/", include("testcase.urls")),
    path("io_module/", include("io_module.urls")),
    path("api/", include("api.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
