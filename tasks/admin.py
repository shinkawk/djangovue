from django.contrib import admin

from .models import Task

@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    list_display=  ('id', 'name', 'disc', 'arn', 'created_at', 'updated_at')
    fields = ('name', 'disc', 'arn')

    class Meta:
        ordering = ('id')