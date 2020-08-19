from tools.generic_class import GenericClass
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from datetime import datetime


# Create your models here.
class User(GenericClass):
    refer_client = models.ForeignKey('client.Client', verbose_name=_('client'), related_name="back_user_client", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name=_("name"))
    color = models.CharField(max_length=8, default='#FF0000')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.refer_client:
            if self not in self.refer_client.users.all():
                self.refer_client.users.add(self)
                self.refer_client.save()
        if self.author:
            self.author.users.add(self)
            self.author.save()

    def __str__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('name', )
