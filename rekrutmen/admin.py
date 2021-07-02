from django.contrib import admin
from .models import Member, Role, Job, JobList, Test

admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Job)
admin.site.register(JobList)
admin.site.register(Test)
