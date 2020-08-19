from django.test import TestCase
from tag.models import Tag
# Create your tests here.


class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="tag_1")
        Tag.objects.create(name="tag_2")
        Tag.objects.create(name="tag_3")
        Tag.objects.create(name="tag_4")

    def test(self):
        tag_1 = Client.objects.get(name="tag_1")
        tag_2 = Client.objects.get(name="tag_2")
        tag_3 = Client.objects.get(name="tag_3")
        tag_4 = Client.objects.get(name="tag_4")
