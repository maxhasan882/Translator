from django.shortcuts import render
from rest_framework.views import APIView
from googletrans import Translator


# Create your views here.


def translate(request):
    if request.method == 'POST':
        data = request.POST
        lang = request.POST.get('lang')
        value = data['value']
        translator = Translator()
        translated = translator.translate(value, dest=lang)
        return render(request, 'index.html', {'data': translated.text, 'translation': translated.extra_data})
    return render(request, 'index.html')
