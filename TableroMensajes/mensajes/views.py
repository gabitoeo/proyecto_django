from django.shortcuts import render
from .models import Mensaje
from django.contrib.auth.models import User

def mensajes_recibidos(request):
        request.user.is_authenticated:
        mensajes = Mensaje.objects.filter(destinatario=request.user)
        return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})
