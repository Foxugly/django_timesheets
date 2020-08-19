from django.forms import ModelForm, Textarea
from client.models import Client
from bootstrap_modal_forms.forms import BSModalForm


class CreateClientForm(BSModalForm):
    model = Client

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs['multiple'] = 'multiple'
        self.fields['tags'].widget.attrs['class'] = "selectpicker"
        self.fields['tags'].queryset = user.tags.all()
        self.fields['users'].widget.attrs['multiple'] = 'multiple'
        self.fields['users'].widget.attrs['class'] = "selectpicker"
        self.fields['users'].queryset = user.users.all()

    class Meta:
        model = Client
        fields = ['name', 'tags', 'users', ]


class ClientForm(ModelForm):
    model = Client

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['tags'].widget.attrs['multiple'] = 'multiple'
        self.fields['tags'].widget.attrs['class'] = "selectpicker"
        self.fields['tags'].queryset = user.tags.all()
        self.fields['users'].widget.attrs['multiple'] = 'multiple'
        self.fields['users'].widget.attrs['class'] = "selectpicker"
        self.fields['users'].queryset = user.users.all()
        self.fields['projects'].widget.attrs['multiple'] = "multiple"
        self.fields['projects'].widget.attrs['class'] = "selectpicker"
        self.fields['projects'].queryset = user.projects.all()

    class Meta:
        model = Client
        fields = ['name', 'projects', 'tags',  'users', ]
