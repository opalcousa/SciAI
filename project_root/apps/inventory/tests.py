from django.test import TestCase
from .models import RawMaterial

class RawMaterialModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        RawMaterial.objects.create(name='Test Material', density=1.0, price=100.0)

    def test_name_label(self):
        material = RawMaterial.objects.get(id=1)
        field_label = material._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_density_label(self):
        material = RawMaterial.objects.get(id=1)
        field_label = material._meta.get_field('density').verbose_name
        self.assertEquals(field_label, 'density')

    def test_price_label(self):
        material = RawMaterial.objects.get(id=1)
        field_label = material._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_name_max_length(self):
        material = RawMaterial.objects.get(id=1)
        max_length = material._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        material = RawMaterial.objects.get(id=1)
        expected_object_name = f'{material.name}'
        self.assertEquals(expected_object_name, str(material))