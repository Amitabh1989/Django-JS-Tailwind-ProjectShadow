from django.contrib import admin
from .models import TestStep, TestCase


class TestCaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')
    list_display = [field.name for field in TestCase._meta.fields]
    

class TestStepAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')
    list_display = [field.name for field in TestStep._meta.fields]
    print(f"List display : {TestStep._meta.fields}")

    def module_type(self, obj):
        # Assuming 'step' is a JSONField in the TestStep model
        step_data = obj.step

        # Access the 'module_type' key from the JSON data
        module_value = step_data.get('module_type', None)
        return module_value.upper()

    # Add the custom function to the list_display
    list_display.insert(2, 'module_type')
    search_fields = list_display
    # list_display.append('module_type')

# Register your models here.
admin.site.register(TestStep, TestStepAdmin)
admin.site.register(TestCase, TestCaseAdmin)
