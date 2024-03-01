"""
URL configuration for Bangladesz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from fabryka.views import oddzial, zmiany, dzieci, komentarze, komentarz, komentarz_new, komentarz_edit
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
]
