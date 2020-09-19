from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User

from . models import VehicleModel, VehicleActionModel

#vehicles
class VehicleListView(ListView):
    model = VehicleModel
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return VehicleModel.objects.filter(owner=user)

class VehicleDetailView(DetailView):
    model = VehicleModel
    context_object_name = 'vehicle'


class VehicleAddView(CreateView):
    model= VehicleModel
    fields = ['year', 'vehicle_make', 'vehicle_modeltype','VINNumber','Notes']
    template_name = 'vehicle_add.html'

    def form_valid(self, form):
        form.instance.owner= self.request.user
        return super().form_valid(form)

class VehicleDetailView(UpdateView):
    model = VehicleModel
    # can change fields to match fields of VehicleModel
    fields = ['year', 'vehicle_make', 'vehicle_modeltype','VINNumber','Notes']
    template_name = 'vehiclemodel_detail.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VehicleDeleteView(DeleteView):
    model = VehicleModel
    def get_success_url(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        print(user)
        return reverse('app_eqpt_records:vehicle_list',kwargs={'username':user.username})



###actions###

class VehicleActionListView(ListView):
    model = VehicleActionModel
    template_name = 'vehicle_record.html'
    context_object_name = 'events'


    def get_queryset(self):
        veh = get_object_or_404(VehicleModel, id = self.kwargs.get('pk'),)
        return VehicleActionModel.objects.filter(Vehicle=veh)

class VehicleActionView(UpdateView):
    model = VehicleActionModel
    # can change fields to match fields of VehicleModel
    fields = ['ActionDate', 'Description', 'Cost']
    template_name = 'vehiclemodel_action_detail.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
