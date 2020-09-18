from django.urls import path
from . import views

app_name = 'app_eqpt_records'

urlpatterns = [
    path('<str:username>/vehicles/', views.VehicleListView.as_view(), name='vehicle_list'),

    ]


#vehicledetailview/notesview
#vehiclerecordview
#vehicleactionview
