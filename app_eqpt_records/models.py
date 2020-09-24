from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class VehicleModel(models.Model):

    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    year = models.IntegerField()
    vehicle_make = models.CharField(max_length=200)
    vehicle_modeltype = models.CharField(max_length=200)
    liscence_plate = models.CharField(max_length=200)
    Notes = models.TextField(null=True)
    Placeholder = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.owner) + ' / ' + str(self.year) + ' / ' +self.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:vehicle_detail', kwargs = {'username':str(self.owner), 'pk':self.pk})
        # return reverse('app_eqpt_records:vehicle_list', kwargs= {'username':str(self.owner)})

# class VehicleActionModel(models.Model):
#     Vehicle = models.ForeignKey(VehicleModel, on_delete = models.CASCADE)
#     ActionDate = models.DateField()
#     Description = models.TextField(null=True)
#     Cost = models.FloatField()
#
#     def __str__(self):
#         return(str(self.Vehicle.owner) + ' / ' + str(self.ActionDate) + ' / '+ str(self.Vehicle.year) +' ' + self.Vehicle.vehicle_modeltype)
#
#     def get_absolute_url(self):
#         return reverse('app_eqpt_records:vehicle_action', kwargs = {'username':str(self.Vehicle.owner), 'pk':self.pk, 'rk':self.pk})

class VehicleActionModel(models.Model):
    Vehicle = models.ForeignKey(VehicleModel, on_delete = models.CASCADE)
    ActionDate = models.DateField()
    Description = models.TextField(null=True)
    Cost = models.FloatField()
    Title = models.CharField(max_length=200, null=True)
    Placeholder = models.BooleanField(default=False)

    def __str__(self):
        return(str(self.Vehicle.owner) + ' / ' + str(self.ActionDate) + ' / '+ str(self.Vehicle.year) +' ' + self.Vehicle.vehicle_modeltype)

    def get_absolute_url(self):
        return reverse('app_eqpt_records:vehicle_action', kwargs = {'username':str(self.Vehicle.owner), 'pk':self.pk, 'rk':self.pk})
