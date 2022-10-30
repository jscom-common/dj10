from django.shortcuts import render
import googletrans
from googletrans import Translator

# Create your views here.
def index(request) :
    inp = request.GET.get('inp', '')
    s1 = request.GET.get('sel1', '')
    s2 = request.GET.get('sel2', '')
    b = googletrans.LANGUAGES
    if inp :
        translator = Translator()
        trans = translator.translate(inp, src=s1, dest=s2)
        res = trans.text
    else :
        res = ''
    context = {}
    context.update({
        'inp' : inp,
        'sel1' : s1,
        'sel2' : s2,
        'res' : res,
        'b' : b,
    })
    return render(request, 'trans/index.html', context)
