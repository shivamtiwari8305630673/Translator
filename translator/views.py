from django.shortcuts import render
from googletrans import Translator
from .models import TranslationHistory

def translate_text(request):
    translation = None
    error = None
    if request.method == 'POST':
        text = request.POST.get('text')
        lang = request.POST.get('language')
        if text and lang:
            try:
                translator = Translator()
                translated = translator.translate(text, dest=lang)
                translation = translated.text
                TranslationHistory.objects.create(
                    input_text=text,
                    translated_text=translation,
                    target_language=lang
                )
            except Exception as e:
                error = f"Translation failed: {e}"
        else:
            error = "Please enter text and select a language."
    return render(request, 'translate.html', {'translation': translation,})