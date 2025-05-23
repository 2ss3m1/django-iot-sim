from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')
def sensor_data_view(request):
    return render(request, 'sensors/sensor_data.html')
