from warnings import onceregistry

from django.db import models
from django.urls import reverse
# Create your models here.
class Osoba(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def get_detail_url(self):
        return reverse('osoba', args=(self.pk,))

class Wydawca(models.Model):
    nazwa = models.CharField(max_length=200)


class Rola(models.Model):
    aktor = models.ForeignKey(Osoba, on_delete=models.CASCADE, related_name='role')
    film = models.ForeignKey("Film", on_delete=models.CASCADE, related_name='wystapili')
    rola = models.CharField(max_length=200)


class Film(models.Model):
    tytul = models.CharField(max_length=200)
    rok = models.IntegerField()
    rezyser = models.ForeignKey(Osoba, on_delete=models.CASCADE, related_name='wyrezyserowal')
    scenarzysta = models.ForeignKey(Osoba, on_delete=models.CASCADE, related_name='filmy_scenariusze')