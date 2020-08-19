from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj not in list(request.user.users.all()):
            request.user.users.add(obj)


admin.site.register(User, UserAdmin)
