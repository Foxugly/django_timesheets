from tools.generic_views import *
from client.models import Client
from client.forms import ClientForm, CreateClientForm
from django.utils.translation import gettext as _
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Client
    fields = None
    form_class = CreateClientForm
    template_name = 'update_modal.html'
    success_message = 'Success: new client created.'
    success_url = reverse_lazy('client:client_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

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

class ClientListView(LoginRequiredMixin, GenericListView):
    model = Client
    template_name = 'list_client.html'

    def get_queryset(self):
        queryset = self.request.user.clients.all().order_by('id')
        return queryset


class ClientUpdateView(LoginRequiredMixin, GenericUpdateView):
    model = Client
    fields = None
    form_class = ClientForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ClientDetailView(LoginRequiredMixin, GenericDetailView):
    model = Client
    template_name = 'detail_client.html'


class ClientDeleteView(LoginRequiredMixin, GenericDeleteView):
    model = Client
