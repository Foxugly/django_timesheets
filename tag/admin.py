from django.contrib import admin
from tag.models import Tag


# Register your models here.
class TagAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj not in list(request.user.tags.all()):
            request.user.tags.add(obj)


admin.site.register(Tag, TagAdmin)
