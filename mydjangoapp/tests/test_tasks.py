import requests_mock

from django.test import TestCase

from apps.core.models import Contest
from apps.core.tasks import fetch_contests, PCI_URL


class FetchContestsTaskTest(TestCase):
    def test_create_contests_from_fetch(self):
        html = """
            <div class='caixa-organizador'>
                <ul>
                    <li>Concurso C</li>
                    <li>Concurso D</li>
                </ul>
            </div>
        """
        with requests_mock.Mocker() as m:
            m.get(PCI_URL, text=html)
            fetch_contests()

        titles = set(Contest.objects.values_list("title", flat=True))
        assert titles == {"Concurso C", "Concurso D"}

