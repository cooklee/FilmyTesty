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
