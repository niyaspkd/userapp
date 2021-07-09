from django.test import TestCase
from rest_framework import status
from django.urls import reverse

# Crefrom myapp.models import Animal
from .models import User
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework.test import APIClient,APITestCase
from django.contrib.auth.models import User
from .views import UserView, UserUpdate
from rest_framework.authtoken.models import Token
from django.urls import resolve

class UserTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', phoneNumber="918075678265",email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_soft_delete(self):
        self.assertEqual(self.user.soft_delete, False)

    def test_phone_number(self):
        self.assertEqual(len(self.user.phoneNumber),12)
    
    def test_resolution_for_list_create(self):
        resolver = resolve('/users/list')
        self.assertEqual(resolver.func.cls, UserView)

    
    def test_resolution_for_update(self):
        resolver = resolve('/users/detail/1')
        self.assertEqual(resolver.func.cls, UserUpdate)
