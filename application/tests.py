from django.test import TestCase
from application.models import Application
import random
import unittest

class AppTestCase(TestCase):
    def setUp(self):
        for x in range(0, 1000):
            Application.objects.create(title=str(x), description="roar",link="sdfs",price=0.0,photo="http://www.joomlaworks.net/images/demos/galleries/abstract/7.jpg")
    def test_apps(self):
        for x in range(0,1000):
            temp = Application.objects.get(title=str(x))
            self.assertEqual(temp.title, temp.__str__(),"title did not match temp's title")
            self.assertIsInstance(temp,Application)