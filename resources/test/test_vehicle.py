from django.test import TestCase
from resources.models import Vehicle

class VehicleTests(TestCase):
    fixtures = ['vehicle_fixture']

    def setUp(self):
        self.vehicle = Vehicle.objects.get(pk=1)

    def test_vehicle_is_activate_must_be_true(self):
        #import pdb; pdb.set_trace()
        self.assertTrue(self.vehicle.is_activate)
        self.assertEquals(self.vehicle.usecontrols.count(),0)
