from django.db import models

class TranslationHistory(models.Model):
    input_text = models.TextField()
    translated_text = models.TextField()
    target_language = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.input_text[:20]}... -> {self.target_language}"




# Create your models here.
