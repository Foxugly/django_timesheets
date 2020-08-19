from django.contrib import admin
from task.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj not in list(request.user.tasks.all()):
            request.user.tasks.add(obj)

    filter_horizontal = ('tags', 'users')

admin.site.register(Task, TaskAdmin)
