from django.contrib import admin
from .models import IOModule

# Register your models here.
class IOModuleAdmin(admin.ModelAdmin):
    print("IO Module Meta : {}".format(IOModule._meta))
    list_display = [field.name for field in IOModule._meta.fields]
admin.site.register(IOModule, IOModuleAdmin)
