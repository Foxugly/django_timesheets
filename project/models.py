from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from tag.models import Tag
from task.models import Task
from timesheet.models import Timesheet
from tools.generic_class import GenericClass
from user.models import User


class Project(GenericClass):
    name = models.CharField(max_length=50, verbose_name=_("name"), )
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name=_("description"), )
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"), )
    users = models.ManyToManyField(User, blank=True, verbose_name=_("users"), )
    refer_client = models.ForeignKey('client.Client', verbose_name=_('client'), related_name="back_project_client",
                                     null=True, on_delete=models.CASCADE, )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, )
    tasks = models.ManyToManyField(Task, blank=True, verbose_name=_("tasks"), )
    timesheets = models.ManyToManyField(Timesheet, blank=True, verbose_name=_("timesheets"), )
    done = models.BooleanField(default=False)
    close_date = models.DateField(blank=True, null=True)

    def get_status(self):
        if self.done:
            if self.close_date <= self.end_date:
                return 3
            else:
                return 4
        elif datetime.now().date() < self.start_date:
            return 0
        elif self.end_date <= datetime.now().date() and datetime.now().date() <= self.end_date:
            return 1
        else:
            return 2

    def get_timesheets(self):
        # print(self.__class__.description.field.verbose_name)
        return self.timesheets.all()

    def get_n_timesheets(self):
        return len(self.get_timesheets())

    def get_total_duration(self):
        out = timedelta(seconds=0)
        for t in self.get_timesheets():
            out += t.get_duration()
        return out

    def get_users(self):
        return self.users.all()

    def get_tags(self):
        return self.tags.all()

    def get_tasks(self):
        return self.tasks.all()

    def save(self, *args, **kwargs):
        if self.done:
            if self.close_date is None:
                self.close_date = datetime.now().date()
        super(Project, self).save(*args, **kwargs)
        if self not in self.refer_client.users.all():
            self.refer_client.projects.add(self)
            self.refer_client.save()
        if self.author:
            self.author.projects.add(self)
            self.author.save()

    def __str__(self):
        return "%s - %s" % (self.refer_client.name, self.name)

    class Meta:
        verbose_name = _('projet')
        verbose_name_plural = _('projects')
        ordering = ('name',)
