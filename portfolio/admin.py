from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_at', 'link') # Fields to display in the list view
    search_fields = ('name', 'description') # Fields to search by
    list_filter = ('created_at',) # Fields to filter by

