from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Contest

PCI_URL = 'https://www.pciconcursos.com.br/'

@shared_task
def fetch_contests():
    response = requests.get(PCI_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # Esta é apenas uma ilustração simplificada
    for item in soup.select('.caixa-organizador li'):
        text = item.get_text(strip=True)
        parts = [p.strip() for p in text.split('|')]
        title = parts[0]
        job_title = parts[1] if len(parts) > 1 else ''
        education = parts[2] if len(parts) > 2 else ''
        salary = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else None

        Contest.objects.get_or_create(
            title=title,
            url=PCI_URL,
            defaults={
                'job_title': job_title,
                'education_level': education,
                'salary': salary,
            },
        )
