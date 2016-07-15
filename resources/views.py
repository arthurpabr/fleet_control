from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from resources.models import Driver, Vehicle, UseControl, Manufacturer

def index(request):
    context_return = {
        'course_name' : 'Python e Django na Prática',
        'alunos_list': [
            {'name' : 'Arthur'},
            {'name' : 'João'},
            {'name' : 'Maria'},
            {'name' : 'Pedro'},
            {'name' : 123456 },
        ],
    }
    return render(request,'hello.html',context_return)

def usecontrol_add(request):
    manufacturer = Manufacturer(name='Fiat')
    manufacturer.save()
    driver = Driver(name = 'Arthur R Marcondes')
    driver.save()
    vehicle = Vehicle(name = 'Grand Siena', licence_plate = 'GMX0102', \
        manufacture_year = date(2007,1,1), manufacturer = manufacturer)
    vehicle.save()
    usecontrol = UseControl(driver = driver, vehicle = vehicle)
    usecontrol.save()
    return HttpResponse('Dados criados com sucesso!')

def usecontrol_list(request):
    # busca o primeiro registro de UseControl
    usecontrol = UseControl.objects.all().first()
    context_return = {
        'vehicle': usecontrol.vehicle.name,
        'driver': usecontrol.driver.name,
        'date_started': usecontrol.date_started
    }
    return render(request, 'usecontrol_list.html', context_return)
