from django.test import TestCase
from resources.models import Vehicle, Manufacturer, UseControl, Driver, Manager
from datetime import date

class UseControlTests(TestCase):
    fixtures = ['manufacturer_fixture']

    def setUp(self):
        self.usecontrol = UseControl.objects.create(
            driver=Driver.objects.create(name='José da Silva'),
            vehicle=Vehicle.objects.create(name='Uno',
                licence_plate='GGG1414',
                manufacture_year=date(2000,1,1),
                manufacturer=Manufacturer.objects.all().first()))

    def test_usecontrol_date_started_dont_be_null(self):
        self.assertNotEqual(self.usecontrol.date_started,None)

    def test_usecontrol_date_ended_must_be_null(self):
        self.assertEqual(self.usecontrol.date_ended,None)
