from django.forms import ModelForm
from .models import ConfigModel

class ConfigForm(ModelForm):
    class Meta:
        model = ConfigModel
        fields = '__all__'