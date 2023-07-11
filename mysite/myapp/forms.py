from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from .models import ConfigModel


class ConfigModelForm(ModelForm):

    class Meta:
        model = ConfigModel
        # name = model.module_type
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_fields = ConfigModel._meta.get_fields()

        for field in model_fields:
            print(f"Field prop : {field}")
            if field.choices:
                choices = [choice for choice in field.choices]
                form_field = forms.ChoiceField(choices=choices)
                self.fields[field.name] = form_field

        css_class = 'module-model-form-class'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = css_class