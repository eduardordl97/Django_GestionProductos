from django.shortcuts import render
from servicios.models import Servicio #importar sServico

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all() #importar todos los servicios
    return render(request, 'servicios/servicios.html',{'servicios':servicios})