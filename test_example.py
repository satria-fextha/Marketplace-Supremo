# Products/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product  # Asegúrate de importar el modelo correcto

class ProductTestCase(TestCase):
    def setUp(self):
        # Aquí puedes configurar cualquier objeto o estado que necesites para tus pruebas.
        self.client = Client()

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))  # Asegúrate de usar el nombre correcto de la URL
        self.assertEqual(response.status_code, 200)

    def test_product_creation(self):
        initial_product_count = Product.objects.count()
        Product.objects.create(name='Test Product', price=10.99)  # Asegúrate de proporcionar los argumentos correctos
        new_product_count = Product.objects.count()
        self.assertEqual(new_product_count, initial_product_count + 1)

        # chat/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Message  # Asegúrate de importar el modelo correcto

class ChatTestCase(TestCase):
    def setUp(self):
        # Aquí puedes configurar cualquier objeto o estado que necesites para tus pruebas.
        self.client = Client()

    def test_message_list_view(self):
        response = self.client.get(reverse('message_list'))  # Asegúrate de usar el nombre correcto de la URL
        self.assertEqual(response.status_code, 200)

    def test_message_creation(self):
        initial_message_count = Message.objects.count()
        Message.objects.create(content='Hello, world!', user_id=1)  # Asegúrate de proporcionar los argumentos correctos
        new_message_count = Message.objects.count()
        self.assertEqual(new_message_count, initial_message_count + 1)