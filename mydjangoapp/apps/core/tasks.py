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
        title = item.get_text(strip=True)
        Contest.objects.get_or_create(title=title, url=PCI_URL)
