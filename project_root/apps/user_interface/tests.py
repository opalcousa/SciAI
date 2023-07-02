from django.test import TestCase
from .models import UserInterface

class UserInterfaceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserInterface.objects.create(title='Test Title', description='Test Description')

    def test_title_content(self):
        ui = UserInterface.objects.get(id=1)
        expected_object_name = f'{ui.title}'
        self.assertEquals(expected_object_name, 'Test Title')

    def test_description_content(self):
        ui = UserInterface.objects.get(id=1)
        expected_object_name = f'{ui.description}'
        self.assertEquals(expected_object_name, 'Test Description')

class UserInterfaceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserInterface.objects.create(title='Test Title', description='Test Description')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/user_interface/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('user_interface'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('user_interface'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user_interface_detail.html')