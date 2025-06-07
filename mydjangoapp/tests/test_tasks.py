import requests_mock

from django.test import TestCase

from apps.core.models import Contest
from apps.core.tasks import fetch_contests, PCI_URL


class FetchContestsTaskTest(TestCase):
    def test_create_contests_from_fetch(self):
        html = """
            <div class='caixa-organizador'>
                <ul>
                    <li>Concurso C | Analista | Superior | 7000</li>
                    <li>Concurso D | Tecnico | Médio | 3000</li>
                </ul>
            </div>
        """
        with requests_mock.Mocker() as m:
            m.get(PCI_URL, text=html)
            fetch_contests()

        c = Contest.objects.get(title="Concurso C")
        assert c.job_title == "Analista"
        assert c.education_level == "Superior"
        assert c.salary == 7000
        d = Contest.objects.get(title="Concurso D")
        assert d.job_title == "Tecnico"
        assert d.education_level == "Médio"
        assert d.salary == 3000

