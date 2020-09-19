from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class VehicleModel(models.Model):

    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    year = models.IntegerField()
    vehicle_make = models.CharField(max_length=200)
    vehicle_modeltype = models.CharField(max_length=200)
    VINNumber = models.CharField(max_length=200)
    Notes = models.TextField(null=True)

    def __str__(self):
        return (str(self.owner) + ' / ' + str(self.year) + ' / ' +self.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:vehicle_detail', kwargs = {'username':str(self.owner), 'pk':self.pk})
        # return reverse('app_eqpt_records:vehicle_list', kwargs= {'username':str(self.owner)})

class VehicleActionModel(models.Model):
    Vehicle = models.ForeignKey(VehicleModel, null= True, on_delete = models.CASCADE)
    ActionDate = models.DateTimeField()
    Description = models.TextField(null=True)
    Cost = models.FloatField()

    def __str__(self):
        return(str(self.Vehicle.owner) + ' / ' + str(self.ActionDate) + ' / '+ str(self.Vehicle.year) +' ' + self.Vehicle.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:vehicle_action', kwargs = {'username':str(self.Vehicle.owner), 'pk':self.pk, 'rk':self.rk})

# class ActionDetailModel(models.model):
#     VehicleAction = models.OneToOnefield(VehicleActionModel, on_delete = models.CASCADE)
#     ActionDetail = models.TextField(null=True)
#
#     def__str__(self):
#         return('note' + self.VehicleAction.VehicleRecord.vehicle.owner + ' / ' + self.VehicleAction.actionDate + ' / '+ self.VehicleAction.VehicleRecord.vehicle.year +' ' self.VehicleAction.VehicleRecord.vehicle.vehicle_modeltype)
#
#     def get_absolute_url(self):
#         return reverse('app_eqpt_records:action_view')
