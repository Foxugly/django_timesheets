from tools.generic_views import *
from task.models import Task
from task.forms import TaskForm, TaskTimesheetFormSet
from django.utils.translation import gettext as _
from project.models import Project
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreateView(LoginRequiredMixin, GenericCreateView):
    model = Task
    fields = None
    form_class = TaskForm
    template_name = 'update_task.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context.update({'add_timesheet' : _("Ajouter une timesheet")})
        context.update({'delete_timesheet' : _("supprimer")})
        if self.request.POST:
            context['timesheets'] = TaskTimesheetFormSet(self.request.POST, instance=self.object)
        else:
            context['timesheets'] = TaskTimesheetFormSet(instance=self.object)
        return context

    def get_initial(self):
        initial = super().get_initial()
        if self.request.GET.get('client_id'):
            initial['refer_client'] = self.request.GET['client_id']
        if self.request.GET.get('project_id'):
            initial['refer_project'] = self.request.GET['project_id'] 
            initial['refer_client'] = get_object_or_404(Project,pk=self.request.GET['project_id']).refer_client.id
        return initial


    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()

        context = self.get_context_data()
        timesheets = context['timesheets']
        for tsform in timesheets:
            if tsform.is_valid():
                ts = tsform.save(commit=False)
                ts.refer_task = f
                ts.author = f.author
                ts.refer_client = f.refer_client
                ts.refer_project = f.refer_project
                for tag in f.tags.all():
                    ts.tags.append(tag)
                for user in f.users.all():
                    ts.users.append(user)
                ts.save()
        return super().form_valid(form)


class TaskListView(LoginRequiredMixin, GenericListView):
    model = Task
    template_name = 'list_task.html'

    def get_queryset(self):
        queryset = self.request.user.tasks.all().order_by('id')
        return queryset


class TaskUpdateView(LoginRequiredMixin, GenericUpdateView):
    model = Task
    fields = None
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class TaskDetailView(LoginRequiredMixin, GenericDetailView):
    model = Task
    template_name = 'detail_task.html'

class TaskDeleteView(LoginRequiredMixin, GenericDeleteView):
    model = Task
