from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.reports.models import Report


@login_required
def report_drain(request):
    if request.method == 'POST':
        Report.objects.create(
            user=request.user,
            location=request.POST['location'],
            description=request.POST['description']
        )
        return redirect('reports:my_reports')
    return render(request, 'report_form.html')

@login_required
def my_reports(request):
    reports = Report.objects.filter(user=request.user)
    return render(request, 'report_list.html', {'reports': reports})
