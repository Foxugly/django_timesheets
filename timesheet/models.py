from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from tag.models import Tag
from tools.generic_class import GenericClass
from user.models import User


class Timesheet(GenericClass):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("name"))
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name=_("description"))
    refer_client = models.ForeignKey('client.Client', verbose_name=_('client'), related_name="back_timesheet_client",
                                     null=True, blank=True, on_delete=models.CASCADE)
    refer_project = models.ForeignKey('project.Project', verbose_name=_("project"),
                                      related_name="back_timesheet_project", null=True, blank=True,
                                      on_delete=models.CASCADE)
    users = models.ManyToManyField(User, blank=True, verbose_name=_("user"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))
    refer_task = models.ForeignKey('task.Task', verbose_name=_('task'), related_name="back_timesheet_task", blank=True,
                                   null=True, on_delete=models.CASCADE, )
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    task_done = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)

    def get_sorted_users(self):
        users_in_task = self.refer_task.users.all()
        users_in_project = self.refer_task.refer_client.users.all()
        users_in_project_not_in_task = set(users_in_project).difference(users_in_task)
        users_in_client = self.refer_client.users.all()
        users_in_client_not_in_project = set(users_in_client).difference(users_in_project)
        d = {'users_in_task': users_in_task, 'users_in_project': users_in_project,
             'users_in_project_not_in_task': users_in_project_not_in_task,
             'users_in_client_not_in_project': users_in_client_not_in_project, 'users in_client': users_in_client}
        return d

    def get_sorted_tags(self):
        tags_in_task = self.refer_task.tags.all()
        tags_in_project = self.refer_task.refer_client.tags.all()
        tags_in_project_not_in_task = set(tags_in_project).difference(tags_in_task)
        tags_in_client = self.refer_client.tags.all()
        tags_in_client_not_in_project = set(tags_in_client).difference(tags_in_project)
        d = {'tags_in_task': tags_in_task, 'tags_in_project': tags_in_project,
             'tags_in_project_not_in_task': tags_in_project_not_in_task,
             'tags_in_client_not_in_project': tags_in_client_not_in_project, 'tags in_client': tags_in_client}
        return d

    def get_duration(self):
        date_end = datetime.combine(self.date, self.end)
        date_start = datetime.combine(self.date, self.start)
        return date_end - date_start

    def get_users(self):
        return self.users.all()

    def get_tags(self):
        return self.tags.all()

    def save(self, *args, **kwargs):
        super(Timesheet, self).save(*args, **kwargs)
        print("save")
        if self.author:
            if self not in self.author.timesheets.all():
                self.author.timesheets.add(self)
                self.author.save()
        if self.refer_project:
            if self not in self.refer_project.timesheets.all():
                self.refer_project.timesheets.add(self)
            if self not in self.refer_project.refer_client.timesheets.all():
                self.refer_project.refer_client.timesheets.add(self)
        if self.refer_client:
            if self not in self.refer_client.timesheets.all():
                self.refer_client.timesheets.add(self)
        # task
        if self.refer_task:
            if self not in self.refer_task.timesheets.all():
                self.refer_task.timesheets.add(self)
            if self.task_done:
                self.refer_task.done = True
                self.refer_task.close_date = self.date
                self.refer_task.save()
        # tag
        for t in self.tags.all():
            if t not in self.refer_task.tags.all():
                self.refer_task.tags.add(t)
            if t not in self.refer_project.tags.all():
                self.refer_project.tags.add(t)
            if self.refer_client.tags.all():
                self.refer_client.tags.add(t)
        # user
        for u in self.users.all():
            if u not in self.refer_task.users.all():
                self.refer_task.users.add(u)
            if u not in self.refer_project.users.all():
                self.refer_project.users.add(u)
            if self.refer_client.users.all():
                self.refer_client.users.add(u)

    def __str__(self):
        l = []
        if self.refer_client:
            l.append(self.refer_client.name)
        if self.refer_project:
            l.append(self.refer_project.name)
        if self.refer_task:
            l.append(self.refer_task.name)
        if self.name:
            l.append(self.name)
        return "[%d] %s" % (self.id, " - ".join(l))

    class Meta:
        verbose_name = _('timesheet')
        verbose_name_plural = _('timesheets')
        ordering = ('name',)
