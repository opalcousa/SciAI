from django.test import TestCase
from .models import Formulation

class FormulationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Formulation.objects.create(name='Test Formulation', description='This is a test formulation')

    def test_name_label(self):
        formulation = Formulation.objects.get(id=1)
        field_label = formulation._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        formulation = Formulation.objects.get(id=1)
        field_label = formulation._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_name_max_length(self):
        formulation = Formulation.objects.get(id=1)
        max_length = formulation._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        formulation = Formulation.objects.get(id=1)
        expected_object_name = f'{formulation.name}'
        self.assertEquals(expected_object_name, str(formulation))

class FormulationViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Formulation.objects.create(name='Test Formulation', description='This is a test formulation')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/formulations/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('formulation-detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('formulation-detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formulation_detail.html')