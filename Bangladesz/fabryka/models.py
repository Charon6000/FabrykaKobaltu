from django.db import models
from django.db.models import CharField, FloatField, IntegerField, ForeignKey, SET_NULL, Model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Oddział(Model):
    nazwa = CharField(max_length=30)
    ceo = CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Oddziały"
    def __str__(self):
        return self.nazwa

class Zmiana(Model):
    stanowisko = CharField(max_length=30)
    zakres_godzin = CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Zmiany"
    def __str__(self):
        return f"{self.stanowisko} {self.zakres_godzin}"

class Dziecko(Model):
    pensja = FloatField()
    st_anorekcji = CharField(max_length=30)
    kolor = CharField(max_length=20)
    choroby = CharField(max_length=200)
    wiek = IntegerField(validators=(MinValueValidator(4), MaxValueValidator(14)))
    zmiana = ForeignKey('Zmiana', on_delete=SET_NULL, null=True)
    oddział = ForeignKey('Oddział', on_delete = SET_NULL, null=True)
    class Meta:
        verbose_name_plural = "Dzieci"
    def __str__(self):
        return f"{self.id}"

class Komentarz(Model):
    tresc = models.CharField(max_length=200)
    ocena = models.IntegerField()
    data = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Komentarze"
    
    def __str__(self)->str:
        return f"{self.data.day} {self.data.month} {self.data.year} {self.ocena}/10 {self.tresc[:30]}..."