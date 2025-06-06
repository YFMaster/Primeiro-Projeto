from django.test import TestCase
from apps.core.models import Contest

class ContestModelTest(TestCase):
    def test_str(self):
        contest = Contest(title="Teste", url="https://example.com")
        self.assertEqual(str(contest), "Teste")
