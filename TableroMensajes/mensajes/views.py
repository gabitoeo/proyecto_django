from django.shortcuts import render
from .models import Mensaje

def mensajes_recibidos(request):
    mensajes = Mensaje.objects.filter(destinatario='usuario')  # Ajusta según el contexto
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})
