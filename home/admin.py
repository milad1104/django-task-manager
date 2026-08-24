from django.contrib import admin
from .models import Task , Profile

admin.site.register(Profile)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','user')
    search_fields = ('title',)

