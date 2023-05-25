from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from customuser.forms import CustomUserChangeForm, CustomUserCreationForm
from customuser.models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_foo_admin',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_foo_admin')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_foo_admin')}),
        (_('Clients'), {'fields': ('clients', 'projects', 'tags', 'tasks', 'timesheets')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('clients', 'projects', 'tags', 'timesheets')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
