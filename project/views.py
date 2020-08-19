from tools.generic_views import *
from project.models import Project
from project.forms import ProjectForm, CreateProjectForm
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from client.models import Client
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectCreateView(LoginRequiredMixin, GenericCreateView, BSModalCreateView):
    model = Project
    fields = None
    form_class = CreateProjectForm
    template_name = 'update_modal.html'
    success_message = 'Success: new project created.'
    success_url = reverse_lazy('project:project_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        if self.request.GET.get('client_id'):
            initial['refer_client'] = self.request.GET['client']
        return initial

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            return self.request.GET["next"]
        else:
            return self.success_url

class ProjectListView(LoginRequiredMixin, GenericListView):
    model = Project
    template_name = 'list_project.html'

    def get_queryset(self):
        queryset = self.request.user.projects.all().order_by('id')
        return queryset


class ProjectUpdateView(LoginRequiredMixin, GenericUpdateView):
    model = Project
    fields = None
    form_class = ProjectForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ProjectDetailView(LoginRequiredMixin, GenericDetailView):
    model = Project
    template_name = 'detail_project.html'


class ProjectDeleteView(LoginRequiredMixin, GenericDeleteView):
    model = Project
