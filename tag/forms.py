from django.forms import ModelForm, TextInput, CharField
from tag.models import Tag
from collections import OrderedDict


class TagForm(ModelForm):
    model = Tag
    color = CharField(widget=TextInput(attrs={'type': 'color', 'class': 'colorpicker'}))

    class Meta:
        model = Tag
        fields = ['name', 'color']
