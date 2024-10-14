from django.contrib import admin
from .models import Job, JobSource


class JobAdmin(admin.ModelAdmin):
    pass


class JobSourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)
admin.site.register(JobSource, JobSourceAdmin)
