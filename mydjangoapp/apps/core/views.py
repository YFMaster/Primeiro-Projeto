from django.shortcuts import render
from .models import Contest


def contest_list(request):
    contests = Contest.objects.all()
    query = request.GET.get('q')
    if query:
        contests = contests.filter(title__icontains=query)
    state = request.GET.get('state')
    if state:
        contests = contests.filter(state__iexact=state)
    job_title = request.GET.get('job_title')
    if job_title:
        contests = contests.filter(job_title__icontains=job_title)
    education = request.GET.get('education_level')
    if education:
        contests = contests.filter(education_level__icontains=education)
    salary = request.GET.get('salary')
    if salary and salary.isdigit():
        contests = contests.filter(salary__gte=int(salary))
    return render(request, 'contest_list.html', {'contests': contests})
