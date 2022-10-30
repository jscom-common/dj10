from django.shortcuts import render
from gtts import gTTS
import googletrans

# Create your views here.
def index(request) :
    context = {
        'ndict' : googletrans.LANGUAGES
    }
    if request.method == 'POST':
        b = request.POST.get('bf')
        l = request.POST.get('lang')
        f = request.POST.get('fname')
        tts = gTTS(b, lang=l)
        tts.save(f'media/{f}.mp3')
        context.update({
            'bf' : b,
            'lang' : l,
            'fname' : f
        })
    return render(request, 'tts/index.html')