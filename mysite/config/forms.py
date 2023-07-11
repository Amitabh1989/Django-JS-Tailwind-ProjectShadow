from django.forms import ModelForm
from .models import ConfigModel
from django import forms
class ConfigForm(ModelForm):
    class Meta:
        model = ConfigModel
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        model_fields = ConfigModel._meta.get_fields()
        print("Model fileds are : {}".format(model_fields))
        print("Model fileds are : {}".format(ConfigModel._meta.fields))

        for field in model_fields:
            if field.choices:
                form_field = forms.ChoiceField(choices=field.choices)
                self.fields[field.name] = form_field
        
        css_class = 'module-model-form-class'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = css_class