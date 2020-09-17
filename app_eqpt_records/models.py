from django.db import models

# Create your models here.

class VehicleModel(models.Model):

    owner = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    year = models.IntegerField()
    vehicle_make = models.CharField()
    vehicle_modeltype = models.CharField()
    VINNumber = models.CharField()
    Notes = models.TextField(null=True)

    def __str__(self):
        return (self.owner + ' / ' +self.year+ ' / ' +self.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:vehicle_list')


class VehicleRecordModel(models.model):
    vehicle = models.OneToOneField(VehicleModel, on_delete=models.CASCADE)

    def __str__(self):
        return ('record'+ ' / 'self.vehicle.owner + ' / ' +self.vehicle.year+ ' ' +self.vehicle.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:vehicle_view')

class VehicleActionModel(models.model):
    VehicleRecord = models.ForeignKey(VehicleRecordModel, on_delete=models.CASCADE)
    actionDate = models.DateTimeField()
    description = models.TextField(null=True)
    cost = models.FloatField()

    def __str__(self):
        return(self.VehicleRecord.vehicle.owner + ' / ' + self.actionDate + ' / '+ self.VehicleRecord.vehicle.year +' ' self.VehicleRecord.vehicle.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:vehicle_view')

class ActionDetailModel(models.model):
    VehicleAction = models.OneToOnefield(VehicleActionModel, on_delete = models.CASCADE)
    ActionDetail = models.TextField(null=True)

    def__str__(self):
        return('note' + self.VehicleAction.VehicleRecord.vehicle.owner + ' / ' + self.VehicleAction.actionDate + ' / '+ self.VehicleAction.VehicleRecord.vehicle.year +' ' self.VehicleAction.VehicleRecord.vehicle.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:action_view')
