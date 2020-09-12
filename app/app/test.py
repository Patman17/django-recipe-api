from django.test import TestCase

from app.calc import add

class Calctests(TestCase):

    def test_add_numbers(self):
        """Test that 2 numbers added together"""
        self.assertEqual(add(3,8),11)
        