from rest_framework import serializers
from .models import IOModel


class IOModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IOModel
        fields = '__all__'
        read_only_fields = ["module_type"]

    # def get_fields(self):
    #     fields = super().get_fields()
        
    #     # Set default values for the form fields
    #     fields['qd'].default = 1
    #     fields['raidlevel'].default = 'R0'
    #     fields['journal'].default = '--v compat'
    #     fields['pattern'].default = 'xoxo'
    #     fields['random'].default = 50
    #     fields['read'].default = 1
    #     fields['runtime'].default = '-1'
    #     fields['size'].default = '128'
    #     fields['step_wait'].default = '30'
    #     fields['expected_result'].default = 'pass'

    #     return fields
    # def __init__(self, *args, **kwargs):
    #     # default = kwargs.pop('default', False)
    #     super().__init__(*args, **kwargs)

    #     # if default:
    #     self.fields['qd'].default = 1
    #     self.fields['raidlevel'].default = 'R0'
    #     self.fields['journal'].default = '--v compat'
    #     self.fields['pattern'].default = 'xoxo'
    #     self.fields['random'].default = 50
    #     self.fields['read'].default = 1
    #     self.fields['runtime'].default = '-1'
    #     self.fields['size'].default = '128'
    #     self.fields['step_wait'].default = '30'
    #     self.fields['expected_result'].default = 'pass'