from django.test import TestCase
from resources.models import Manager
from datetime import date

class ManagerControlModelTests(TestCase):
    fixtures = ['manager_fixture']

    def test_manager_control_relations(self):
        man_ctrl = Manager.objects.all().first()
        #import pdb; pdb.set_trace()
        self.assertEqual(man_ctrl.user.id, 1)
        self.assertEqual(man_ctrl.user.username, 'joaop')
