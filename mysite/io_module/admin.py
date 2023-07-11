from django.contrib import admin
from .models import IOModel

# Register your models here.
class IOModelAdmin(admin.ModelAdmin):
    print("IO Module Meta : {}".format(IOModel._meta))
    list_display = [field.name for field in IOModel._meta.fields]
admin.site.register(IOModel, IOModelAdmin)
