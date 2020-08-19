from tools.generic_views import *
from timesheet.models import Timesheet
from django.utils.translation import gettext as _
from timesheet.forms import TimesheetForm
from django.shortcuts import get_object_or_404
from task.models import Task
from project.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class TimesheetCreateView(LoginRequiredMixin, GenericCreateView):
    model = Timesheet
    fields = None
    form_class = TimesheetForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        if self.request.GET.get('client_id'):
            initial['refer_client'] = self.request.GET['client_id']
        if self.request.GET.get('project_id'):
            initial['refer_project'] = self.request.GET['project_id'] 
            initial['refer_client'] = get_object_or_404(Project,pk=self.request.GET['project_id']).refer_client.id
        if self.request.GET.get('task_id'):
            initial['refer_task'] = self.request.GET['task_id'] 
            initial['refer_project'] = get_object_or_404(Task,pk=self.request.GET['task_id']).refer_project.id
            initial['refer_client'] = get_object_or_404(Task,pk=self.request.GET['task_id']).refer_project.refer_client.id
        return initial

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super().form_valid(form)


class TimesheetListView(LoginRequiredMixin, GenericListView):
    model = Timesheet


class TimesheetUpdateView(LoginRequiredMixin, GenericUpdateView):
    model = Timesheet
    fields = None
    form_class = TimesheetForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class TimesheetDetailView(LoginRequiredMixin, GenericDetailView):
    model = Timesheet
    template_name = 'detail_timesheet.html'


class TimesheetDeleteView(LoginRequiredMixin, GenericDeleteView):
    model = Timesheet
