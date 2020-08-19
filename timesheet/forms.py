from tools.generic_class import GenericClass
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
#from tag.models import Tag
#from user.models import User
from timesheet.models import Timesheet
from django.forms import ModelForm, DurationField, TextInput, CharField, Textarea, DateInput, TimeInput
from task.models import Task
from collections import OrderedDict
from durationwidget.widgets import TimeDurationWidget


class DateInput(DateInput):
    input_type = 'date'


class TimeInput(TimeInput):
    input_type = 'time'


class TimesheetForm(ModelForm):
    model = Timesheet

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['description'].widget = Textarea(attrs={'cols': 80, 'rows': 4})
        # tags
        self.fields['tags'].widget.attrs['multiple'] = 'multiple'
        self.fields['tags'].widget.attrs['class'] = "selectpicker"
        self.fields['tags'].queryset = user.tags.all()
        l_tags_dict = OrderedDict()
        if instance.pk:
            d = instance.get_sorted_tags()
            for t in d['tags_in_task']:
                try:
                    l_tags_dict['In the task'].append((t.pk, t.name))
                except KeyError:
                    l_tags_dict['In the task'] = [(t.pk, t.name)]
            for t in d['tags_in_project_not_in_task']:
                try:
                    l_tags_dict['In the project'].append((t.pk, t.name))
                except KeyError:
                    l_tags_dict['In the project'] = [(t.pk, t.name)]  
            for t in d['tags_in_client_not_in_project']:
                try:
                    l_tags_dict['Not yet in the project'].append((t.pk, t.name))
                except KeyError:
                    l_tags_dict['Not yet in the project'] = [(t.pk, t.name)]
            self.fields['tags'].choices = l_tags_dict.items()
        else:
            self.fields['tags'].queryset = user.tags.all()
        # users
        self.fields['users'].widget.attrs['multiple'] = 'multiple'
        self.fields['users'].widget.attrs['class'] = "selectpicker"
        l_users_dict = OrderedDict()
        users_in_project = []
        if instance.pk:
            d = instance.get_sorted_users()
            for u in d['users_in_task']:
                try:
                    l_users_dict['In the task'].append((u.pk, u.name))
                except KeyError:
                    l_users_dict['In the task'] = [(u.pk, u.name)]
            for u in d['users_in_project_not_in_task']:
                try:
                    l_users_dict['In the project'].append((u.pk, u.name))
                except KeyError:
                    l_users_dict['In the project'] = [(u.pk, u.name)]  
            for u in d['users_in_client_not_in_project']:
                try:
                    l_users_dict['Not yet in the project'].append((u.pk, u.name))
                except KeyError:
                    l_users_dict['Not yet in the project'] = [(u.pk, u.name)]
            self.fields['users'].choices = l_users_dict.items()
        else:
            self.fields['users'].queryset = user.users.all()


    class Meta:
        model = Timesheet
        fields = ['name', 'description', 'refer_client', 'refer_project', 'refer_task', 'users', 'tags', 'date', 'start', 'end', 'task_done']
        widgets = {
            'date': DateInput(), 'start' : TimeInput(), 'end': TimeInput()
        }


class TimesheetQuickForm(ModelForm):
    model = Timesheet

    class Meta:
        model = Timesheet
        fields = ['name', 'date', 'start', 'end', 'task_done']
        widgets = {
            'date': DateInput(), 'start' : TimeInput(), 'end': TimeInput()
        }