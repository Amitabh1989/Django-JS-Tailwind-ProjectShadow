from django.forms import ModelForm
from config.models import ConfigModel
from django import forms

class ConfigModelForm(ModelForm):
    class Meta:
        model = ConfigModel
        name = model.module_type.field.get_default()
        fields = '__all__'
        exclude = ['_use_count']
        print("Module name is : {}".format(name))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_fields = ConfigModel._meta.get_fields()

        for field in model_fields:
            if field.choices:
                form_field = forms.ChoiceField(choices=field.choices)
                self.fields[field.name] = form_field        

        css_class = 'module-model-form-class'

        for field_name, field in self.fields.items():
            print(f"Applying style {field}")
            field.widget.attrs['class'] = css_class
        
        print("Config => Fields : {}".format(self.fields))