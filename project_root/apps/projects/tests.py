from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(name='Test Project', description='This is a test project')

    def test_name_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name(self):
        project = Project.objects.get(id=1)
        expected_object_name = f'{project.name}'
        self.assertEqual(expected_object_name, str(project))

class ProjectViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(name='Test Project', description='This is a test project')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_detail.html')