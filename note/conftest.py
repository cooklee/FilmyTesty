import pytest
from django.contrib.auth.models import User
from django.test import Client
from note.models import Osoba, Wydawca


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def osoby():
    for x in range(10):
        Osoba.objects.create(imie=f'imie_{x}', nazwisko=f"nazwisko_{x}")
    return Osoba.objects.all()

@pytest.fixture
def wydawcy():
    for x in range(10):
        Wydawca.objects.create(nazwa=f"nazwa_{x}")
    return Wydawca.objects.all()


@pytest.fixture
def user():
    u = User.objects.create(username='cooklee')
    u.set_password("ala")
    u.save()
    return u

