from django.contrib import admin

from apps.reports.models import Report

@admin.register(Report)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ['location', 'status']
    search_fields = ['location', 'description']
    list_filter = ['status']
