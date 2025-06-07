from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from apps.core.models import Contest, Favorite


@login_required
def add_favorite(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    Favorite.objects.get_or_create(user=request.user, contest=contest)
    return HttpResponseRedirect(reverse('contest_list'))


@login_required
def remove_favorite(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    Favorite.objects.filter(user=request.user, contest=contest).delete()
    return HttpResponseRedirect(reverse('contest_list'))
