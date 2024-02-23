from django.contrib import admin
from .models import Oddział,Dziecko,Zmiana,Komentarz

# Register your models here.
admin.site.register(Oddział)
admin.site.register(Dziecko)
admin.site.register(Zmiana)
admin.site.register(Komentarz)