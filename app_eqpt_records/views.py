from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User

from . models import VehicleModel, VehicleActionModel


def create_place_holder_action():

    vehicle_with_action = []
    for vehicle in VehicleActionModel.objects.all():
        vehicle_with_action.append(vehicle.Vehicle)

    for vehicle in VehicleModel.objects.all():
        if vehicle not in vehicle_with_action:
            #create VehicleActionModelObjectHere
            VehicleActionModel.objects.create(Vehicle=vehicle, ActionDate = '1000-01-01', Cost=0)

create_place_holder_action()

#vehicles
class VehicleListView(ListView):
    model = VehicleModel
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'


    def get_queryset(self):
        create_place_holder_action()
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return VehicleModel.objects.filter(owner=user)

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
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

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
    context_object_name = 'actions'

    def get_queryset(self):
        veh = get_object_or_404(VehicleModel, id = self.kwargs.get('pk'))
        return VehicleActionModel.objects.filter(Vehicle=veh)

class VehicleActionAddView(CreateView):
    model= VehicleActionModel
    fields = ['ActionDate', 'Description', 'Cost']
    template_name = 'vehicle_action_add.html'

    def form_valid(self, form):
        # print('request_dict_keys:')
        # print(self.request.__dict__.keys())
        #
        # print('request_resolver_match_keys:')
        # print(self.request.resolver_match.kwargs['pk'])

        form.instance.owner= self.request.user
        # form.instance.post = Post.objects.get(pk=self.kwargs.get("pk"))
        # form.instance.Vehicle = VehicleModel.objects.get(pk=self.kwargs.get("pk"))
        form.instance.Vehicle = VehicleModel.objects.filter(id=self.request.resolver_match.kwargs['pk'])[0]
        return super().form_valid(form)

class VehicleActionDetailView(UpdateView):
    model = VehicleActionModel
    # can change fields to match fields of VehicleModel
    fields = ['ActionDate', 'Description', 'Cost']
    template_name = 'vehiclemodel_action_detail.html'
    def form_valid(self, form):
        form.instance.owner= self.request.user
        form.instance.Vehicle = VehicleModel.objects.filter(id=self.request.resolver_match.kwargs['pk'])[0]
        return super().form_valid(form)
