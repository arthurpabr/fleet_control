from django.test import TestCase
from resources.models import Vehicle, Manufacturer
from datetime import date

class VehicleViewTests(TestCase):
    fixtures = ['vehicle_fixture']

    def setUp(self):
        self.manufacturer = Manufacturer.objects.all().first()

    def test_vehicle_list(self):
        response = self.client.get('/resources/vehicle/list/')
        self.assertEquals(response.status_code, 200)

    def test_must_create_vehicle(self):
        data = {
            'name': 'Uno',
            'description': 'Carro básico, sem frescura',
            'licence_plate': 'GGG1414',
            'manufacture_year': '2000-01-01',
            'manufacturer' : self.manufacturer.id
        }
        response = self.client.post('/resources/vehicle/add/', data)
        self.assertEquals(response.status_code, 302)
        vehicle_saved = Vehicle.objects.all().last()
        # já existe um objeto criado pela fixture; logo, o que foi criado
        # pelo post acima terá id = 2
        self.assertEquals(vehicle_saved.id, 2)
        self.assertEquals(vehicle_saved.name, 'Uno')

    def test_must_delete_vehicle(self):
        response = self.client.post('/resources/vehicle/1/delete/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Vehicle.objects.filter(pk=1).exists(),False)

    def test_must_delete_vehicle(self):
        #import pdb; pdb.set_trace()
        response = self.client.post('/resources/vehicle/1/delete/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Vehicle.objects.filter(pk=1).exists(),False)
        self.assertEquals(Vehicle.objects.all().count(),0)

    def test_must_update_vehicle(self):
        data = {
            'name': 'Grand Siena 1.6',
            'description': Vehicle.objects.all().first().description,
            'licence_plate': Vehicle.objects.all().first().licence_plate,
            'manufacture_year': Vehicle.objects.all().first().manufacture_year,
            'manufacturer' : Vehicle.objects.all().first().manufacturer.id
        }
        #import pdb; pdb.set_trace()
        response = self.client.post('/resources/vehicle/1/', data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Vehicle.objects.all().first().name,'Grand Siena 1.6')
