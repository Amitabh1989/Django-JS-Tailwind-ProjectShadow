from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from .models import IOModel

class IOModelForm(ModelForm):
    class Meta:
        model = IOModel
        name = model.module_type.field.get_default()
        fields = '__all__'
        exclude = ['_use_count']
        print("Module name is : {}".format(name))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_fields = IOModel._meta.get_fields()

        for field in model_fields:
            if field.choices:
                form_field = forms.ChoiceField(choices=field.choices)
                self.fields[field.name] = form_field
        

        css_class = 'module-model-form-class'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = css_class
            # print("IO => Field name : {}   Fields : {}".format(field_name, field))
            # if field_name == 'module_type':
            #     self.fields['module_type'].widget = forms.TextInput(attrs={'readonly':'readonly'})
        
        print("IO => Fields : {}".format(self.fields))
    

        # instance = kwargs.get('module_type')
        # print("Instance is : {}".format(instance))
        # if instance:
        #     print("Instance is : {}".format(instance))
        #     self.fields['module_type'].widget.attrs['value'] = instance.module_type
        #     self.fields['module_type'].widget = forms.TextInput(attrs={'readonly':'readonly'})