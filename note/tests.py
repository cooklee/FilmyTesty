from django.urls import reverse
from note.models import Osoba
import pytest



def test_czy_to_dziala(client):
    result = client.get("/")
    assert result.status_code == 200

@pytest.mark.django_db
def test_osoby_list(client, osoby):
    result = client.get(reverse("osoby_list"))
    assert result.status_code == 200
    assert osoby.count() == result.context['object_list'].count()
    for item in result.context['object_list']:
        assert item in osoby


@pytest.mark.django_db
def test_osoby_list(client, wydawcy):
    result = client.get(reverse("wydawcy_list"))
    assert result.status_code == 200
    assert wydawcy.count() == result.context['object_list'].count()
    for item in result.context['object_list']:
        assert item in wydawcy

@pytest.mark.django_db
def test_dodaj_osoby(client):
    osoba = {'imie':'ala', 'nazwisko':'makota'}
    result = client.post(reverse("dodaj_osoby"), osoba)
    assert result.status_code == 302
    Osoba.objects.get(imie=osoba['imie'], nazwisko=osoba['nazwisko'])


@pytest.mark.django_db
def test_dodaj_wydawce(client):
    wydawca = {'nazwa':'ala'}
    result = client.post(reverse("dodaj_wydawcy"), wydawca)
    assert result.status_code == 302
    Osoba.objects.get(nazwa=wydawca['nazwa'])