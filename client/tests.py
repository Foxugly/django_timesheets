from django.test import TestCase
from client.models import Client
# Create your tests here.


class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name="Alpha")
        Client.objects.create(name="Beta")

    def test(self):
        alpha = Client.objects.get(name="Alpha")
        beta = Client.objects.get(name="Beta")
