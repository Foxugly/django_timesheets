from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj not in list(request.user.projects.all()):
            request.user.projects.add(obj)
            request.user.save()

    filter_horizontal = ('tags', 'users')


admin.site.register(Project, ProjectAdmin)
