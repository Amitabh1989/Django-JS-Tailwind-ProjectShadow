from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from .models import ConfigModel


class ConfigModelForm(ModelForm):

    class Meta:
        model = ConfigModel
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_fields = ConfigModel._meta.get_fields()

        for field in model_fields:
            if field.choices:
                choices = [choice for choice in field.choices]
                print("ConfigForm : Choices : {}".format(choices))
                form_field = forms.ChoiceField(choices=choices)
                print("Self.fields : {}".format(self.fields))
                self.fields[field.name] = form_field

        css_class = 'module-model-form-class'
        # css_attrs = {'class': css_class}

        for field_name, field in self.fields.items():
            print("ConfigForm : Field_name : {}   ==>  Field : {}".format(field_name, field))
            field.widget.attrs['class'] = css_class