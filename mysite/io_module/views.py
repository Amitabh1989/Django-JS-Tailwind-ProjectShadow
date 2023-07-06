from django.shortcuts import render
from django.views.generic import CreateView
from .models import IOModule
from .forms import IOModuleForm

# Create your views here.

class IOModuleView(CreateView):
    model = IOModule
    form_class = IOModuleForm
    template_name = "io_module/io.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module_name'] = self.model.module_type.field.get_default()
        return context

