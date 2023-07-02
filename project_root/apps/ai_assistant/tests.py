from django.test import TestCase
from .models import AIAssistant
from .views import get_ai_response

class AIAssistantModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AIAssistant.objects.create(question='What is the density of water?', answer='1 g/cm^3')

    def test_question_content(self):
        ai_assistant = AIAssistant.objects.get(id=1)
        expected_object_name = f'{ai_assistant.question}'
        self.assertEquals(expected_object_name, 'What is the density of water?')

    def test_answer_content(self):
        ai_assistant = AIAssistant.objects.get(id=1)
        expected_object_name = f'{ai_assistant.answer}'
        self.assertEquals(expected_object_name, '1 g/cm^3')

class AIAssistantViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AIAssistant.objects.create(question='What is the density of water?', answer='1 g/cm^3')

    def test_get_ai_response(self):
        response = self.client.get('/ai_assistant/')
        self.assertEqual(response.status_code, 200)

    def test_get_ai_response_content(self):
        response = self.client.get('/ai_assistant/')
        self.assertContains(response, '1 g/cm^3')