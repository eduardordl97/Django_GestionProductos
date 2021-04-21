from django.contrib import admin
from .models import Servicio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #mostrat campos solo lectura

admin.site.register(Servicio,ServicioAdmin)