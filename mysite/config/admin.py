from django.contrib import admin
from .models import ConfigModel
# Register your models here.

class ConfigModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConfigModel._meta.fields]

admin.site.register(ConfigModel, ConfigModelAdmin)
