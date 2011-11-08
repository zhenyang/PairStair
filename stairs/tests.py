"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from stairs.models import Programmer, Pairing


class ModelTest(TestCase):
    def setUp(self):
        self.yz = Programmer(name='yangzhen')
        self.yz.save()
        self.jason = Programmer(name='jason')
        self.jason.save()
        self.yz.add_pairing_with(self.jason)

    def test_create_programmer(self):
        self.assertEqual(self.yz.name, 'yangzhen')
        self.assertIsNotNone(Programmer.objects.get(name='yangzhen'))

    def test_create_pairing(self):
        self.assertIsNotNone(Pairing.objects.get(programmerOne=self.yz))

    def test_get_pairing_count(self):
        self.assertEqual(self.yz.get_count_paired_with(self.jason), 1)

    def test_add_pairing(self):
        self.yz.add_pairing_with(self.jason)
        self.assertEqual(self.yz.get_count_paired_with(self.jason), 2)
        self.jason.add_pairing_with(self.yz)
        self.assertEqual(self.yz.get_count_paired_with(self.jason), 3)


class TestViews(TestCase):
    def test_should_render_page_to_add_programmer(self):
        response = Client().get('/add_programmer/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_programmer.html')

    def test_should_add_a_programmer(self):
        Client().post('/add_programmer/', {'programmer_name': 'Happy'})

        self.assertIsNotNone(Programmer.objects.get(name='Happy'))

    def test_should_clear_stair(self):
        programmer_one = Programmer(name='one')
        programmer_two = Programmer(name='two')
        programmer_one.save()
        programmer_two.save()
        Pairing(programmerOne=programmer_one, programmerTwo=programmer_two).save()

        Client().get('/clear_stair/')

        self.assertEqual(Programmer.objects.all().count(), 0)
        self.assertEqual(Pairing.objects.all().count(), 0)
