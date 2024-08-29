from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    texto = models.TextField()
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De: {self.remitente} - Para: {self.destinatario} - {self.fecha_envio}"
