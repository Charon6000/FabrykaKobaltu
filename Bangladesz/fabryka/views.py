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
    
    if ocena_max:
        komentarze = komentarze.filter(ocena__lte = ocena_max )

    if ocena_min:
        komentarze = komentarze.filter(ocena__gte = ocena_min)

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
    zgoda = True
    context = {}
    if request.method == "POST":
        tresc = request.POST.get("tresc")
        ocena = request.POST.get("ocena")
        
        if ocena:
            if int(ocena)<1 or int(ocena)>10:
                zgoda = False
                context['ocenawarning'] = "Ocena ma mieścić się w zakresie od 1-10"
                context['tresc'] = tresc
                context['ocena']=ocena
        
        if tresc:
            if len(tresc)>99 or tresc == None:
                zgoda=False
                context['trescwarning'] = "Tresc ma mieć mniej niż 99 znaków"
                context['tresc'] = tresc
                context['ocena']=ocena
        
        if zgoda:
            kom = Komentarz(tresc = tresc, ocena = ocena)
            try:
                kom.save()
                return redirect("komentarze")
            except:
                pass
    return render(request, "fabryka/komentarz_new.html", context)

@csrf_exempt
def komentarz_edit(request, id):
    komentarz = Komentarz.objects.get(id=id)
    zgoda = True
    context={
        'komentarz': komentarz,
    }
    if request.method == "POST":
        tresc = request.POST.get("tresc")
        ocena = request.POST.get("ocena")
        
        if ocena:
            if int(ocena)<1 or int(ocena)>10:
                zgoda = False
                context['ocenawarning'] = "Ocena ma mieścić się w zakresie od 1-10"
                context['tresc'] = tresc
                context['ocena']=ocena
        
        if tresc:
            if len(tresc)>99 or tresc == None:
                zgoda=False
                context['trescwarning'] = "Tresc ma mieć mniej niż 99 znaków"
                context['tresc'] = tresc
                context['ocena']=ocena
        
        if zgoda:
            kom = Komentarz(id=id, tresc = tresc, ocena = ocena)
            try:
                kom.save()
                return redirect("komentarze/"+id)
            except:
                pass
    return render(request, "fabryka/komentarz_edit.html", context)