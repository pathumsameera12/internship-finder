from django.contrib import admin
from . models import *

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_id', 'time_date', 'job_type', 'location')  # Customize the fields displayed in the list view
    list_filter = ('job_type', 'location')  # Add filters to the right sidebar
    search_fields = ('title', 'description', 'location')  # Add a search bar
    date_hierarchy = 'time_date'  # Add a date-based drilldown navigation by time_date

    fieldsets = (
        ('General Information', {
            'fields': ('title', 'description', 'job_id')
        }),
        ('Job Details', {
            'fields': ('email', 'time_date', 'skill', 'job_type', 'location')
        }),
    )

admin.site.register(Job, JobAdmin)
