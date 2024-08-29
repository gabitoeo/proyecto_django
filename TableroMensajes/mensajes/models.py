from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    texto = models.TextField()
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
