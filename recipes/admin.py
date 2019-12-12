from django.contrib import admin

from .models import Recipe
# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display=  ('name', 'disc', 'task1', 'task2', 'task3', 'task4',
    'task5', 'task6', 'task7', 'task8', 'task9', 'task10', 
    'created_at', 'updated_at')
    fields = ('name', 'disc', 'task1', 'task2', 'task3', 'task4',
    'task5', 'task6', 'task7', 'task8', 'task9', 'task10')

    class Meta:
        ordering = ('created_at')