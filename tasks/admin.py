from django.contrib import admin
from tasks.models import Task,List

admin.site.register(Task,None)
admin.site.register(List,None)

# Register your models here.
