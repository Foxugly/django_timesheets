from django.forms import ModelForm, DurationField, TextInput, CharField, Textarea
from task.models import Task
from timesheet.models import Timesheet
from collections import OrderedDict
from durationwidget.widgets import TimeDurationWidget
from timesheet.forms import TimesheetQuickForm
from django.forms import inlineformset_factory


class TaskForm(ModelForm):
    model = Task

    duration = DurationField(widget=TimeDurationWidget(show_days=True, show_hours=True, show_minutes=True, show_seconds=False), required=False)
    start_date = CharField(widget=TextInput(attrs={'type': 'date'}))
    end_date = CharField(widget=TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
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
        self.fields['refer_project'].widget.attrs['class'] = "selectpicker"
        self.fields['refer_project'].queryset = user.projects.all()
        self.fields['duration'].widget.attrs['class'] = "form-control timeduration"
        self.fields['description'].widget = Textarea(attrs={'cols': 80, 'rows': 4})

    class Meta:
        model = Task
        fields = ['name', 'description', 'refer_client', 'refer_project', 'users', 'tags', 'duration', 'start_date', 'end_date', 'done']

TaskTimesheetFormSet = inlineformset_factory(Task, Timesheet, form=TimesheetQuickForm, extra=1,)