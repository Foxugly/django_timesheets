
from django.contrib import admin
from timesheet.models import Timesheet
# Register your models here.


class TimesheetAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj not in list(request.user.timesheets.all()):
            request.user.timesheets.add(obj)

    filter_horizontal = ('tags',)


admin.site.register(Timesheet, TimesheetAdmin)
