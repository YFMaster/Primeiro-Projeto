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
    return render(request, 'contest_list.html', {'contests': contests})
