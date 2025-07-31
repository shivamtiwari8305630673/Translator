# translator_project/settings.py
# (Assuming default settings, add 'translator' to INSTALLED_APPS)

# translator/models.py
from django.db import models

class TranslationHistory(models.Model):
    input_text = models.TextField()
    translated_text = models.TextField()
    target_language = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.input_text[:20]}... -> {self.target_language}"


# translator/views.py
from django.shortcuts import render
from googletrans import Translator
from .models import TranslationHistory

def translate_text(request):
    translation = None
    if request.method == 'POST':
        text = request.POST.get('text')
        lang = request.POST.get('language')
        translator = Translator()
        translated = translator.translate(text, dest=lang)
        translation = translated.text

        # Save history
        TranslationHistory.objects.create(
            input_text=text,
            translated_text=translation,
            target_language=lang
        )

    return render(request, 'translate.html', {'translation': translation})


# translator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.translate_text, name='translate'),
]


# translator/templates/translate.html
<!DOCTYPE html>
<html>
<head>
    <title>Translator App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script>
        function startDictation() {
            if (window.hasOwnProperty('webkitSpeechRecognition')) {
                var recognition = new webkitSpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.lang = "en-US";
                recognition.start();

                recognition.onresult = function(e) {
                    document.getElementById('textInput').value = e.results[0][0].transcript;
                    recognition.stop();
                };

                recognition.onerror = function(e) {
                    recognition.stop();
                }
            }
        }
    </script>
</head>
<body class="container py-5">
    <h1 class="mb-4">Language Translator</h1>
    <form method="post">
        {% csrf_token %}
        <div class="mb-3">
            <label>Enter Text:</label>
            <textarea id="textInput" name="text" class="form-control" rows="4"></textarea>
            <button type="button" onclick="startDictation()" class="btn btn-secondary mt-2">🎤 Speak</button>
        </div>
        <div class="mb-3">
            <label>Select Language:</label>
            <select name="language" class="form-control">
                <option value="hi">Hindi</option>
                <option value="fr">French</option>
                <option value="de">German</option>
                <option value="en">English</option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Translate</button>
    </form>

    {% if translation %}
        <div class="alert alert-success mt-4">
            <h4>Translated Text:</h4>
            <p>{{ translation }}</p>
        </div>
    {% endif %}
</body>
</html>


# translator_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('translator.urls')),
]


# Requirements (requirements.txt)
django
googletrans==4.0.0-rc1
