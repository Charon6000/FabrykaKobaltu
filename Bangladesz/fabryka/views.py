from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Oddział
from .models import Dziecko
from .models import Zmiana
from .models import Komentarz

# Create your views here.

def oddzial(request):
    oddzialy = Oddział.objects.all()
    context = {
        'oddzialy': oddzialy,
    }
    return render(request, 'fabryka/oddzial.html', context)

def dzieci(request):
    dziecko = Dziecko.objects.all()
    context = {
        'dzieci': dziecko,
    }
    return render(request, 'fabryka/dzieci.html', context)

def zmiany(request):
    zmiany = Zmiana.objects.all()
    context = {
        'zmiany': zmiany,
    }
    return render(request, 'fabryka/zmiany.html', context)

def komentarze(request):
    ocena_min = request.GET.get('ocena_min')
    ocena_max = request.GET.get('ocena_max')

    komentarze = Komentarz.objects.all()
    
    if ocena_min:
        komentarze = Komentarz.objects.filter(ocena__lte = ocena_max )

    if ocena_max:
        komentarze = Komentarz.objects.filter(ocena__gte = ocena_min)

    context={
        'komentarze': komentarze,
    }
    return render(request, "fabryka/komentarze.html", context)

def komentarz(request, id):
    komentarz = Komentarz.objects.get(id=id)
    context={
        'komentarz': komentarz,
    }
    return render(request, "fabryka/komentarz.html", context)

@csrf_exempt
def komentarz_new(request):
    if request.method == "POST":
        tresc = request.POST.get("tresc")
        ocena = request.POST.get("ocena")
        # if ocena<1 or ocena>10:

        kom = Komentarz(tresc = tresc, ocena = ocena)
        try:
            kom.save()
            return redirect("komentarze")
        except:
            pass
    return render(request, "fabryka/komentarz_new.html")