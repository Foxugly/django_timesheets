from tools.generic_class import GenericClass
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


# Create your models here.
class Tag(GenericClass):
    name = models.CharField(max_length=20, verbose_name=_("name"))
    color = models.CharField(max_length=8, default='#FF0000')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s" % (self.name,)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.author:
            self.author.tags.add(self)
            self.author.save()

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        ordering = ('name', )
