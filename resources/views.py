from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
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

class UseControlListView(TemplateView):
    template_name = 'usecontrol_list.html'

    def get_context_data(self, **kwargs):
        context = super(UseControlListView, self).get_context_data(**kwargs)
        usecontrol = UseControl.objects.all().last()
        context['vehicle'] = usecontrol.vehicle.name
        context['driver'] = usecontrol.driver.name
        context['date_started'] = usecontrol.date_started
        return context

class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name','description','licence_plate','manufacture_year','manufacturer']

class VehicleUpdate(UpdateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['name','description','licence_plate','manufacture_year','manufacturer']

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    template_name = 'vehicle_confirm_delete.html'

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    queryset = Vehicle.objects.order_by('name')
    context_object_name = 'vehicle_list'
    paginate_by = 2

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
