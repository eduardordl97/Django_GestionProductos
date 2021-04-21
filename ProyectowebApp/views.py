from django.shortcuts import render, HttpResponse
from servicios.models import Servicio #importar sServico
# Create your views here.

def home(request):

    return render(request, 'ProyectowebApp/home.html')






