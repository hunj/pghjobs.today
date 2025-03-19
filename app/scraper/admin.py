from django.contrib import admin
from .models import JobSource


class JobSourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(JobSource, JobSourceAdmin)
