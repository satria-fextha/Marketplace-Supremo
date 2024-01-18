from django.apps import AppConfig
from django.contrib.auth.models import Group


class UsuariosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "usuarios"
    def ready(self):
        # Register user types
        Group.objects.get_or_create(name='agricultores')
        Group.objects.get_or_create(name='ganaderos')
        Group.objects.get_or_create(name='consumidores')
