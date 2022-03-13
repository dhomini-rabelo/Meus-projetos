from django.contrib import admin
from .models import Project

admin.site.empty_value_display = 'NULL'




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug', 
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = 'name',
