from django.contrib import admin

from .models import Task, Setting

@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    list_display=  ('id', 'name', 'disc', 'arn', 'created_at', 'updated_at')
    fields = ('name', 'disc', 'arn')

    class Meta:
        ordering = ('id')

@admin.register(Setting)
class UserAdmin(admin.ModelAdmin):
    list_display=  ('id', 'task_id', 'data','created_at', 'updated_at' )
    fields = ('task_id', 'data')

    class Meta:
        ordering = ('id')