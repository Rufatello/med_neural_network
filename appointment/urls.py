from django.urls import path
from appointment.apps import AppointmentConfig
from appointment.views import Home

app_name = AppointmentConfig.name

urlpatterns = [
    path('', Home.as_view(), name='home')

]