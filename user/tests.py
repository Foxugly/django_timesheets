from django.test import TestCase
from user.models import User
# Create your tests here.


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(name="user_1")
        User.objects.create(name="user_2")
        User.objects.create(name="user_3")
        User.objects.create(name="user_4")

    def test(self):
        user_1 = User.objects.get(name="user_1")
        user_2 = User.objects.get(name="user_2")
        user_3 = User.objects.get(name="user_3")
        user_4 = User.objects.get(name="user_4")
