from django.test import TestCase
from django.urls import reverse

from apps.core.models import Contest


class ContestListViewTest(TestCase):
    def setUp(self):
        Contest.objects.create(
            title="Concurso A",
            url="https://a.com",
            state="SP",
            job_title="Analista",
            education_level="Superior",
            salary=5000,
        )
        Contest.objects.create(
            title="Concurso B",
            url="https://b.com",
            state="RJ",
            job_title="Tecnico",
            education_level="Médio",
            salary=3000,
        )

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

    def test_filter_by_job_title(self):
        response = self.client.get(reverse("contest_list"), {"job_title": "Analista"})
        assert response.status_code == 200
        content = response.content.decode()
        assert "Concurso A" in content
        assert "Concurso B" not in content

    def test_filter_by_education_level(self):
        response = self.client.get(reverse("contest_list"), {"education_level": "Médio"})
        assert response.status_code == 200
        content = response.content.decode()
        assert "Concurso B" in content
        assert "Concurso A" not in content

    def test_filter_by_salary(self):
        response = self.client.get(reverse("contest_list"), {"salary": "4000"})
        assert response.status_code == 200
        content = response.content.decode()
        assert "Concurso A" in content
        assert "Concurso B" not in content

