from django.urls import path
from . import views

app_name = 'app_eqpt_records'

urlpatterns = [
    path('<str:username>/vehicles/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('<str:username>/vehicles/add', views.VehicleAddView.as_view(), name='vehicle_add'),
    path('<str:username>/vehicles/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
    path('<str:username>/vehicles/<int:pk>/delete', views.VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('<str:username>/vehicles/<int:pk>/records/', views.VehicleActionListView.as_view(), name='vehicle_records'),
    path('<str:username>/vehicles/<int:pk>/records/<int:rk>', views.VehicleActionDetailView.as_view(), name='vehicle_action'),
    path('<str:username>/vehicles/<int:pk>/records/add', views.VehicleActionAddView.as_view(), name='vehicle_action_add'),
    path('<str:username>/vehicles/<int:pk>/records/delete', views.VehicleActionDeleteListView.as_view(), name='vehicle_action_list_delete'),
    path('<str:username>/vehicles/<int:pk>/records/deleteaction', views.delete_action, name='vehicle_action_delete'),

    ]
