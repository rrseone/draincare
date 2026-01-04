from django.urls import path

from apps.reports import views

app_name = 'reports'

urlpatterns = [
    path('new/', views.report_drain, name='create_report'),
    path('my-reports/', views.my_reports, name='my_reports'),
]