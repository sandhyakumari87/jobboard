from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from .models import Application


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    Application.objects.get_or_create(
        job=job,
        applicant=request.user
    )

    return redirect('/')


@login_required
def my_applications(request):
    applications = Application.objects.filter(
        applicant=request.user
    )

    return render(request, 'applications/my_applications.html', {
        'applications': applications
    })


@login_required
def employer_applications(request):
    jobs = Job.objects.filter(employer=request.user)

    applications = Application.objects.filter(
        job__in=jobs
    )

    return render(request, 'applications/employer_applications.html', {
        'applications': applications
    })