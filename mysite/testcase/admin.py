from django.contrib import admin
from .models import TestStep, TestCase


class TestCaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')

class TestStepAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on')

# Register your models here.
admin.site.register(TestStep, TestStepAdmin)
admin.site.register(TestCase, TestCaseAdmin)
