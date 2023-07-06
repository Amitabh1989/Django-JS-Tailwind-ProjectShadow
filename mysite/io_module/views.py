from django.shortcuts import render
from django.views.generic import CreateView
from .models import IOModule
from .forms import IOModuleForm

# Create your views here.

class IOModuleView(CreateView):
    model = IOModule
    form_class = IOModuleForm
    template_name = "io_module/io.html"
