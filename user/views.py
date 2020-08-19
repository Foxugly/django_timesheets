from tools.generic_views import *
from user.models import User
from user.forms import UserForm
from django.utils.translation import gettext as _
from timesheet.models import Timesheet
from task.models import Task
from project.models import Project
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin



class UserCreateView(LoginRequiredMixin, GenericCreateView):
    model = User
    fields = None
    form_class = UserForm
    src = {}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        if self.request.GET.get('client_id'):
            self.src['client'] = self.request.GET['client_id']
        elif self.request.GET.get('project_id'):
            self.src['project'] = self.request.GET['project_id']
        elif self.request.GET.get('task_id'):
            self.src['task'] = self.request.GET['task_id']
        elif self.request.GET.get('timesheet_id'):
            self.src['timesheet'] = self.request.GET['timesheet_id']
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        if self.request.GET.get('client_id'):
            initial['refer_client'] = self.request.GET['client_id']
        elif self.request.GET.get('project_id'):
            initial['refer_client'] = get_object_or_404(Project,pk=self.request.GET['project_id']).refer_client.id
        elif self.request.GET.get('task_id'):
            initial['refer_client'] = get_object_or_404(Task,pk=self.request.GET['task_id']).refer_client.id
        elif self.request.GET.get('timesheet_id'):    
            initial['refer_client'] = get_object_or_404(Timesheet,pk=self.request.GET['timesheet_id']).refer_client.id
        return initial


    def form_valid(self, form):
        response = super().form_valid(form)
        inst = self.object
        if len(self.src):
            if 'client' in self.src:
                c = Client.objects.get(id=self.src['client'])
                c.users.add(inst)
            elif 'project' in self.src:
                p = Project.objects.get(id=self.src['project'])
                if inst not in p.users.all():
                    p.users.add(inst)
                if inst not in p.refer_client.users.all():
                    p.refer_client.users.add(inst)
            elif 'task' in self.src:
                t = Task.objects.get(id=self.src['task'])
                if inst not in t.users.all():
                    t.users.add(inst)
                if inst not in t.refer_project.users.all():
                    t.refer_project.users.add(inst)
                if inst not in t.refer_project.refer_client.users.all():
                    t.refer_project.refer_client.users.add(inst)
            elif 'timesheet' in self.src:
                ts = Timesheet.objects.get(id=self.src['timesheet'])
                if inst not in ts.users.all():
                    ts.users.add(inst)
                if inst not in ts.refer_task.users.all():
                    ts.refer_task.users.add(inst)    
                if inst not in ts.refer_task.refer_project.users.all():
                    ts.refer_task.refer_project.users.add(inst)
                if inst not in ts.refer_task.refer_project.refer_client.users.all():
                    ts.refer_task.refer_project.refer_client.users.add(inst)
            self.src.clear()
        return response


class UserListView(LoginRequiredMixin, GenericListView):
    model = User
    template_name = 'list_user.html'

    def get_queryset(self):
        queryset = self.request.user.users.all().order_by('id')
        return queryset


class UserUpdateView(LoginRequiredMixin, GenericUpdateView):
    model = User
    fields = None
    form_class = UserForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UserDetailView(LoginRequiredMixin, GenericDetailView):
    model = User


class UserDeleteView(LoginRequiredMixin, GenericDeleteView):
    model = User
