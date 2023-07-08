from django.contrib import admin
from .models import TestStep, TestCase


class TestCaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')
    # list_display = [field.name for field in TestCase._meta.fields]

class TestStepAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')
    # list_display = [field.name for field in TestCase._meta.fields]

# Register your models here.
admin.site.register(TestStep, TestStepAdmin)
admin.site.register(TestCase, TestCaseAdmin)
