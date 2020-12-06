import pytest
from django.test import Client
from note.models import Osoba

@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def osoby():
    for x in range(10):
        Osoba.objects.create(imie=f'imie_{x}', nazwisko=f"nazwisko_{x}")
    return Osoba.objects.all()
