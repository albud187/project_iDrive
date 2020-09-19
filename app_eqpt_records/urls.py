from django.urls import path
from . import views

app_name = 'app_eqpt_records'

urlpatterns = [
    path('<str:username>/vehicles/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('<str:username>/vehicles/add', views.VehicleAddView.as_view(), name='vehicle_add'),
    # path('<str:username>/vehicles/', views.VehicleDetailView.as_view(), name='vehicle_detail'),


    ]

#vehicleadd
#vehicledetailview/notesview
#vehiclerecordview
#vehicleactionview
