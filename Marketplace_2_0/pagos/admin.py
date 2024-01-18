from django.contrib import admin

from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'customer']
    list_filter = ['status']
    search_fields = ['id', 'customer__username']

admin.site.register(Order, OrderAdmin)


# Register your models here.
