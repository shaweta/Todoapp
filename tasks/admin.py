from django.contrib import admin
from .models import Tasks
# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display=['task_name','due_date','is_completed','created_on','updated_on']

admin.site.register(Tasks,TasksAdmin)
