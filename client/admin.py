from django.contrib import admin
from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    #def save_model(self, request, obj, form, change):
    #    super().save_model(request, obj, form, change)
    #    if obj not in list(request.user.clients.all()):
    #        request.user.clients.add(obj)

    filter_horizontal = ('projects', 'tags', 'users')


admin.site.register(Client, ClientAdmin)
