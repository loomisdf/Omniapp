from django.test import TestCase
from user.models import User
import random
import unittest

class AppTestCase(TestCase):
    def setUp(self):
        for x in range(0, 1000):
            User.objects.create(username=str(x), password=str(x),email=str(x))
    def test_user(self):
        for x in range(0,1000):
            temp = User.objects.get(username=str(x))
            self.assertEqual(temp.username, temp.__str__(),"username did not match temp's username")
            self.assertEqual(temp.password, str(x),"password did not match temp's password")
            self.assertEqual(temp.email, str(x),"email did not match temp's email")
            self.assertIsInstance(temp,User)