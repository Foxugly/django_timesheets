from tools.generic_class import GenericClass
from django.db import models
from django.utils.translation import gettext as _
from tag.models import Tag
from project.models import Project
from user.models import User
from task.models import Task
from timesheet.models import Timesheet
from django.conf import settings
from datetime import timedelta

# Create your models here.
class Client(GenericClass):

    name = models.CharField(max_length=100, verbose_name=_("name"), )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))
    projects = models.ManyToManyField(Project, blank=True, verbose_name=_("projects"), )
    tasks = models.ManyToManyField(Task, blank=True, verbose_name=_("tasks"), )
    timesheets = models.ManyToManyField(Timesheet, blank=True, verbose_name=_("timesheets"), )
    users = models.ManyToManyField(User, blank=True, verbose_name=_("users"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, )

    def get_projects(self):
        return self.projects.all()
        
    def get_timesheets(self):
        return self.timesheets.all()

    def get_n_timesheets(self):
        return len(self.get_timesheets())

    def get_total_duration(self):
        out = timedelta(seconds=0)
        for t in self.get_timesheets():
            out+= t.get_duration()
        return out

    def get_users(self):
        return self.users.all()

    def get_tags(self):
        return self.tags.all()

    def get_tasks(self):
        return self.tasks.all()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.author:
            self.author.clients.add(self)
            self.author.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')
        ordering = ('name',)
