from django.contrib import admin

# Register your models here.

from . models import VehicleModel, VehicleRecordModel, VehicleActionModel

admin.site.register(VehicleModel)
admin.site.register(VehicleRecordModel)
admin.site.register(VehicleActionModel)
