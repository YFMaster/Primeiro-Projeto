from django.test import TestCase
from django.urls import reverse

from apps.core.models import Contest


class ContestListViewTest(TestCase):
    def setUp(self):
        Contest.objects.create(title="Concurso A", url="https://a.com", state="SP")
        Contest.objects.create(title="Concurso B", url="https://b.com", state="RJ")

    def test_status_ok(self):
        response = self.client.get(reverse("contest_list"))
        assert response.status_code == 200

    def test_filter_by_query(self):
        response = self.client.get(reverse("contest_list"), {"q": "Concurso A"})
        assert response.status_code == 200
        content = response.content.decode()
        assert "Concurso A" in content
        assert "Concurso B" not in content

    def test_filter_by_state(self):
        response = self.client.get(reverse("contest_list"), {"state": "RJ"})
        assert response.status_code == 200
        content = response.content.decode()
        assert "Concurso B" in content
        assert "Concurso A" not in content

