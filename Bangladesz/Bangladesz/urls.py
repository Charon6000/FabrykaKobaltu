from django.contrib import admin
from fabryka.views import oddzial, zmiany, dzieci, komentarze, komentarz, komentarz_new, komentarz_edit, komentarz_delete
from django.urls import path

urlpatterns = [
    path('', oddzial, name="oddziały"),
    path('admin/', admin.site.urls),
    path('oddzial', oddzial, name="oddziały"),
    path('dzieci', dzieci, name="dzieci"),
    path('zmiany', zmiany, name="zmiany"),
    path('komentarze', komentarze, name="komentarze"),
    path('komentarz/<int:id>', komentarz, name="komentarz"),
    path('komentarz/<int:id>/edit', komentarz_edit, name="komentarz_edit"),
    path('komentarz_new', komentarz_new, name="komentarz_new"),
    path('komentarz/<int:id>/delete', komentarz_delete, name="komentarz_delete"),
]
