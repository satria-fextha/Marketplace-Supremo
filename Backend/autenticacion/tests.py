from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTestCase(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.farmer = self.User.objects.create_user(
            email='farmer@example.com',
            password='password',
            user_type='farmer'
        )
        self.livestock_owner = self.User.objects.create_user(
            email='owner@example.com',
            password='password',
            user_type='livestock_owner'
        )
        self.consumer = self.User.objects.create_user(
            email='consumer@example.com',
            password='password',
            user_type='consumer'
        )

    def test_create_user(self):
        self.assertEqual(self.farmer.email, 'farmer@example.com')
        self.assertEqual(self.livestock_owner.email, 'owner@example.com')
        self.assertEqual(self.consumer.email, 'consumer@example.com')

    def test_update_user(self):
        self.farmer.email = 'new_farmer@example.com'
        self.farmer.save()
        self.assertEqual(self.farmer.email, 'new_farmer@example.com')

    def test_delete_user(self):
        self.consumer.delete()
        self.assertEqual(self.User.objects.filter(email='consumer@example.com').count(), 0)

    def test_authentication(self):
        farmer = self.User.objects.get(email='farmer@example.com')
        self.assertTrue(farmer.check_password('password'))


# Create your tests here.
