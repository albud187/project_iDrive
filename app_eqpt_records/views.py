from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from . models import VehicleModel, VehicleRecordModel, VehicleActionModel

class VehicleListView(ListView):
    model = VehicleModel
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return VehicleModel.objects.filter(owner=user)
