from django.forms import ModelForm, TextInput, CharField
from user.models import User


class UserForm(ModelForm):
    model = User
    color = CharField(widget=TextInput(attrs={'type': 'color', 'class': 'colorpicker'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['refer_client'].queryset = user.clients.all()

    class Meta:
        model = User
        fields = ['name', 'color', 'refer_client']
