from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Job


def job_list(request):
    jobs = Job.objects.all()

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs
    })

@login_required
def add_job(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']

        Job.objects.create(
            title=title,
            description=description,
            location=location,
            employer=request.user
        )

        return redirect('/')

    return render(request, 'jobs/add_job.html')