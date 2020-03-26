from django.shortcuts import render
from django.views import generic
from .models import Bancar

class BancarList(generic.ListView):
    model = Bancar
    template_name = 'blog/index.html'

# Create your views here.
