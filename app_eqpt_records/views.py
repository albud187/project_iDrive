from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from . models import VehicleModel, VehicleRecordModel, VehicleActionModel
from .forms import VehicleUpdateForm
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
    fields = ['VINNumber','year','Notes']
    template_name = 'vehiclemodel_detail.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VehicleDeleteView(DeleteView):
    model = VehicleModel
    success_url =''
