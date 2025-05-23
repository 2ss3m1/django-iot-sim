from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('live-data/', views.sensor_data_view, name='sensor_data'),

]
