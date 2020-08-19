from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from project.models import Project
from client.models import Client
from tag.models import Tag
from user.models import User
from task.models import Task
from timesheet.models import Timesheet


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password):
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    language = models.CharField(_("language"), max_length=8, choices=settings.LANGUAGES, default=1)
    is_foo_admin = models.BooleanField(_("Foo admin"), default=False, help_text=_('Designates users that are foo Admin.'),)
    clients = models.ManyToManyField(Client, blank=True, verbose_name=_("clients"))
    projects = models.ManyToManyField(Project, blank=True, verbose_name=_("projects"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))
    tasks = models.ManyToManyField(Task, blank=True, verbose_name=_("taches"))
    users = models.ManyToManyField(User, blank=True, verbose_name=_("users"))
    timesheets = models.ManyToManyField(Timesheet, blank=True, verbose_name=_("timesheets"))
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
