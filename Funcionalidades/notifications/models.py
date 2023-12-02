
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    is_read = models.BooleanField(default=False)

    class Type(models.TextChoices):
        MESSAGE = 'message', 'Mensaje'
        ORDER_STATUS_CHANGE = 'order_status_change', 'Cambio de estado del pedido'
        PROMOTION = 'promotion', 'Promoción'

    type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.MESSAGE,
    )

    def __str__(self):
        return self.message
