from django.forms import ModelForm
from .models import ConfigModel


class ConfigModelForm(ModelForm):
    class Meta:
        model = ConfigModel
        fields = "__all__"