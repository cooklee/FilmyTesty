from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from note.models import Osoba


def index(request):
    return render(request, 'base.html')
# Create your views here.


class OsobaListView(ListView):
    model = Osoba
    template_name = 'list_view.html'


class DodajOsobeView(CreateView):
    model = Osoba
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('osoby_list')


class OsobaView(DetailView):
    model = Osoba
    template_name = 'detail.html'
