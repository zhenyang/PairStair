"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from stairs.models import Programmers


class ModelTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        pgr=Programmers(name='asdf')
        pgr.save()
        self.assertEqual(pgr.name,'asdf')
        self.assertIsNotNone(Programmers.objects.get(name='asdf'))
