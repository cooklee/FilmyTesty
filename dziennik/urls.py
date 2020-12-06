"""dziennik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from note import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('osoby/', views.OsobaListView.as_view(), name='osoby_list'),
    path('wydawcy/', views.WydawcaListView.as_view(), name='wydawcy_list'),
    path('dodaj_osoby/', views.DodajOsobeView.as_view(), name='dodaj_osoby'),
    path('dodaj_wydawcy/', views.DodajWydawcaView.as_view(), name='dodaj_wydawcy'),
    path('osoba/<int:pk>', views.OsobaView.as_view(), name='osoba'),
]
