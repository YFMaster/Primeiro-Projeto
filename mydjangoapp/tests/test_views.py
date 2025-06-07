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

    def test_export_pdf(self):
        weasyprint = __import__('importlib').import_module('importlib').import_module('weasyprint') if __import__('importlib').import_module('importlib').util.find_spec('weasyprint') else None
        if not weasyprint:
            self.skipTest('weasyprint not installed')
        response = self.client.get(reverse("contest_export") + "?format=pdf")
        assert response.status_code == 200
        assert response['Content-Type'] == 'application/pdf'
        assert response.content.startswith(b'%PDF')

    def test_export_excel(self):
        openpyxl_spec = __import__('importlib').import_module('importlib').util.find_spec('openpyxl')
        if not openpyxl_spec:
            self.skipTest('openpyxl not installed')
        response = self.client.get(reverse("contest_export") + "?format=excel")
        assert response.status_code == 200
        assert response['Content-Type'].startswith('application/vnd.openxmlformats')


