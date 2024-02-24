#from django.test import TestCase
from unittest import TestCase

from tasks.forms import SimpleForm


class MainTest(TestCase):
    def test_field_email(self):
        form_not_bound = SimpleForm()
        form = SimpleForm(data={"name": "pepito", "email": "lala@example.es"})

        self.assertFalse(form_not_bound.is_bound)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
        self.assertIsNotNone(form.errors)

        print(form.errors)
        print(form.cleaned_data)

        self.assertIsNotNone(form.cleaned_data)


