from tools.generic_class import GenericClass
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from tag.models import Tag
from user.models import User
from timesheet.models import Timesheet
from datetime import timedelta, datetime

# Create your models here.
class Task(GenericClass):
    name = models.CharField(max_length=100, verbose_name=_("name"), blank= True, null=True)
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name=_("description"), )
    duration = models.DurationField(verbose_name=_("estimated duration"), blank= True, null=True)
    refer_client = models.ForeignKey('client.Client', verbose_name=_('client'), related_name="back_task_client", null=True, on_delete=models.CASCADE, )
    refer_project = models.ForeignKey('project.Project', verbose_name=_('project'), related_name="back_task_project", null=True, on_delete=models.CASCADE, )
    users = models.ManyToManyField(User, blank=True, verbose_name=_("users"), )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"), )
    start_date = models.DateField(null=True, blank=True, verbose_name=_("start date"), )
    end_date = models.DateField(null=True, blank=True, verbose_name=_("end date"), )
    timesheets = models.ManyToManyField(Timesheet, blank=True, verbose_name=_("timesheets"), )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    done = models.BooleanField(default=False)
    close_date = models.DateField(null=True, blank=True, verbose_name=_("close date"), )

    def get_status(self):
        if self.done:
            if self.close_date <= self.end_date:
                return 3
            else:
                return 4
        elif datetime.now().date() < self.start_date:
            return 0
        elif self.start_date <= datetime.now().date() and datetime.now().date() <= self.end_date:
            return 1
        else:
            return 2

    def get_users(self):
        return self.users.all()

    def get_tags(self):
        return self.tags.all()

    def get_timesheets(self):
        return self.timesheets.all()

    def get_n_timesheets(self):
        return len(self.get_timesheets())

    def get_total_duration(self):
        out = timedelta(seconds=0)
        for t in self.get_timesheets():
            out+= t.get_duration()
        return out

    def __str__(self):
        l = []
        if self.refer_client:
            l.append(self.refer_client.name)
        if self.refer_project:
            l.append(self.refer_project.name)
        if self.name:
            l.append(self.name)
        return "[%d] %s" % (self.id, " - ".join(l))

    def save(self, *args, **kwargs):
        if self.done and not self.close_date:
            self.close_date = datetime.now().date()
        super().save(*args, **kwargs)
        if self.author:
            if self not in self.author.tasks.all():
                self.author.tasks.add(self)
                self.author.save()
        if self.refer_client:
            if self not in self.refer_client.tasks.all():
                self.refer_client.tasks.add(self)
        if self.refer_project:
            if self not in self.refer_project.tasks.all():
                self.refer_project.tasks.add(self)

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
        ordering = ('name', )
