import os
import django
from django.contrib.auth.models import User
from mensajes.models import Mensaje

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TableroMensajes.settings')
django.setup()

def crear_datos_prueba():
    # Crear usuarios de prueba
    usuario1, created = User.objects.get_or_create(username='usuario1', defaults={'password': 'password1'})
    usuario2, created = User.objects.get_or_create(username='usuario2', defaults={'password': 'password2'})

    # Crear mensajes de prueba
    Mensaje.objects.get_or_create(texto='Hola, ¿cómo estás?', remitente=usuario1, destinatario=usuario2)
    Mensaje.objects.get_or_create(texto='Estoy bien, gracias. ¿Y tú?', remitente=usuario2, destinatario=usuario1)

    print('Datos de prueba creados exitosamente')

if __name__ == '__main__':
    crear_datos_prueba()
    