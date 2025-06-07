from celery import shared_task
import requests
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from .models import Contest

PCI_URL = 'https://www.pciconcursos.com.br/'

@shared_task
def fetch_contests():
    response = requests.get(PCI_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # Esta é apenas uma ilustração simplificada
        for item in soup.select('.caixa-organizador li'):
            title = item.get_text(strip=True)
            Contest.objects.get_or_create(title=title, url=PCI_URL)


@shared_task
def send_update_email(contest_id: int) -> None:
    """Notify users that a contest was updated."""
    contest = Contest.objects.get(id=contest_id)
    emails = list(contest.favorite_set.select_related('user').values_list('user__email', flat=True))
    if emails:
        send_mail(
            f'Edital atualizado: {contest.title}',
            f'O concurso {contest.title} foi atualizado.',
            'noreply@example.com',
            emails,
            fail_silently=True,
        )
