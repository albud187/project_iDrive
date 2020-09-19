from django.contrib import admin

# Register your models here.

from . models import VehicleModel, VehicleActionModel

admin.site.register(VehicleModel)
admin.site.register(VehicleActionModel)
