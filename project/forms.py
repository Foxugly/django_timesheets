from django.forms import ModelForm, Textarea, CharField, TextInput
from project.models import Project
from collections import OrderedDict
from bootstrap_modal_forms.forms import BSModalForm


class ProjectForm(ModelForm):
    model = Project
    start_date = CharField(widget=TextInput(attrs={'type': 'date'}))
    end_date = CharField(widget=TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        # tags
        self.fields['tags'].widget.attrs['multiple'] = 'multiple'
        self.fields['tags'].widget.attrs['class'] = "selectpicker"
        self.fields['tags'].queryset = user.tags.all()
        l_tags_dict = OrderedDict()
        tags_in_project = []
        if instance.pk:
            tags_in_project = instance.tags.all()
            for t in tags_in_project:
                try:
                    l_tags_dict['in the project'].append((t.pk, t.name))
                except KeyError:
                    l_tags_dict['in the project'] = [(t.pk, t.name)]
            for t in set(instance.refer_client.tags.all()).difference(tags_in_project):
                try:
                    l_tags_dict['not yet in the project'].append((t.pk, t.name))
                except KeyError:
                    l_tags_dict['not yet in the project'] = [(t.pk, t.name)]
            self.fields['tags'].choices = l_tags_dict.items()
        else:
            self.fields['tags'].queryset = user.tags.all()
        # users
        self.fields['users'].widget.attrs['multiple'] = 'multiple'
        self.fields['users'].widget.attrs['class'] = "selectpicker"
        l_users_dict = OrderedDict()
        users_in_project = []
        if instance.pk:
            users_in_project = instance.users.all()
            for u in users_in_project:
                try:
                    l_users_dict['in the project'].append((u.pk, u.name))
                except KeyError:
                    l_users_dict['in the project'] = [(u.pk, u.name)]
            for u in set(instance.refer_client.users.all()).difference(users_in_project):
                try:
                    l_users_dict['not yet in the project'].append((u.pk, u.name))
                except KeyError:
                    l_users_dict['not yet in the project'] = [(u.pk, u.name)]
            self.fields['users'].choices = l_users_dict.items()
        else:
            self.fields['users'].queryset = user.users.all()


        self.fields['refer_client'].widget.attrs['class'] = "selectpicker"
        self.fields['refer_client'].queryset = user.clients.all()
        self.fields['description'].widget = Textarea(attrs={'cols': 80, 'rows': 4})


    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'refer_client', 'users', 'tags', 'done']


class CreateProjectForm(ProjectForm, BSModalForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'refer_client', 'users', 'tags', 'done']
