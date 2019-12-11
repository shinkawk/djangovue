from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=  ('name', 'uid', 'email', 'created_at', 'updated_at')
    fields = ('name', 'email')

    class Meta:
        ordering = ('created_at')