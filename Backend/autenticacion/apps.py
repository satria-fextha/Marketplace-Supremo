from django.apps import AppConfig
from django.apps import AppConfig
from autenticacion.models import Agricultor, Ganadero, Consumidor
from autenticacion.utils import send_verification_email, send_verification_sms
from django.db.models.signals import post_save


class AutenticacionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autenticacion"

    def ready(self):
        import autenticacion.signals  # Import signals module for email/phone verification

        # Implementar la lógica para verificar la autenticidad de los correos electrónicos o números de teléfono
        # y enviar correos o SMS de verificación después del registro
        def create_user(sender, instance, created, **kwargs):
            if created:
                if isinstance(instance, Agricultor):
                    # Implementar la lógica para enviar correos electrónicos de verificación para agricultores
                    send_verification_email(instance.email)
                elif isinstance(instance, Ganadero):
                    # Implementar la lógica para enviar SMS de verificación para ganaderos
                    send_verification_sms(instance.phone_number)
                elif isinstance(instance, Consumidor):
                    # Implementar la lógica para enviar correos electrónicos de verificación para consumidores
                    send_verification_email(instance.email)

        # Registrar el evento de creación de usuario para ejecutar la función create_user
        post_save.connect(create_user, sender=Agricultor)
        post_save.connect(create_user, sender=Ganadero)
        post_save.connect(create_user, sender=Consumidor)
