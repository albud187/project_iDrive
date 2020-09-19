from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
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

class VehicleDetailView(DetailView):
    model = VehicleModel

class VehicleAddView(CreateView):
    model= VehicleModel
    fields = ['year', 'vehicle_make', 'vehicle_modeltype','VINNumber','Notes']
    template_name = 'vehicle_add.html'

    def form_valid(self, form):
        form.instance.owner= self.request.user
        return super().form_valid(form)

class VehicleRecordView(ListView):
    model = VehicleRecordModel
    template_name = 'vehicle_record.html'
    context_object_name = 'vehicle_actions'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        
