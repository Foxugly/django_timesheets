from tools.generic_views import *
from tag.models import Tag
from tag.forms import TagForm
from django.utils.translation import gettext as _
from project.models import Project
from client.models import Client
from task.models import Task
from timesheet.models import Timesheet
from django.contrib.auth.mixins import LoginRequiredMixin


class TagCreateView(LoginRequiredMixin, GenericCreateView):
    model = Tag
    fields = None
    form_class = TagForm
    src = {}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.GET.get('client_id'):
            self.src['client'] = self.request.GET['client_id']
        elif self.request.GET.get('project_id'):
            self.src['project'] = self.request.GET['project_id']
        elif self.request.GET.get('task_id'):
            self.src['task'] = self.request.GET['task_id']
        elif self.request.GET.get('timesheet_id'):
            self.src['timesheet'] = self.request.GET['timesheet_id']
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        inst = self.object
        if len(self.src):
            if 'client' in self.src:
                c = Client.objects.get(id=self.src['client'])
                c.tags.add(inst)
            elif 'project' in self.src:
                p = Project.objects.get(id=self.src['project'])
                if inst not in p.tags.all():
                    p.tags.add(inst)
                if inst not in p.refer_client.tags.all():
                    p.refer_client.tags.add(inst)
            elif 'task' in self.src:
                t = Task.objects.get(id=self.src['task'])
                if inst not in t.tags.all():
                    t.tags.add(inst)
                if inst not in t.refer_project.tags.all():
                    t.refer_project.tags.add(inst)
                if inst not in t.refer_project.refer_client.tags.all():
                    t.refer_project.refer_client.tags.add(inst)
            elif 'timesheet' in self.src:
                ts = Timesheet.objects.get(id=self.src['timesheet'])
                if inst not in ts.tags.all():
                    ts.tags.add(inst)
                if inst not in ts.refer_task.tags.all():
                    ts.refer_task.tags.add(inst)    
                if inst not in ts.refer_task.refer_project.tags.all():
                    ts.refer_task.refer_project.tags.add(inst)
                if inst not in ts.refer_task.refer_project.refer_client.tags.all():
                    ts.refer_task.refer_project.refer_client.tags.add(inst)
            print(self.src)
            self.src.clear()
        return response



class TagListView(LoginRequiredMixin, GenericListView):
    model = Tag
    template_name = 'list_tag.html'
    
    def get_queryset(self):
        queryset = self.request.user.tags.all().order_by('id')
        return queryset


class TagUpdateView(LoginRequiredMixin, GenericUpdateView):
    model = Tag
    fields = None
    form_class = TagForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs


class TagDetailView(LoginRequiredMixin, GenericDetailView):
    model = Tag


class TagDeleteView(LoginRequiredMixin, GenericDeleteView):
    model = Tag
