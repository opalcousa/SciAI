from django.db import models

class AIAssistant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Query(models.Model):
    assistant = models.ForeignKey(AIAssistant, on_delete=models.CASCADE)
    query_text = models.TextField()
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.assistant.name} - {self.query_text[:50]}"