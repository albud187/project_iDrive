from django import forms
from django.contrib.auth.models import User
from .models import VehicleModel

class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = ['Notes']
