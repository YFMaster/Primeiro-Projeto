from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Contest
import io

try:
    import weasyprint  # type: ignore
except Exception:  # pragma: no cover - dependency optional
    weasyprint = None

try:
    from openpyxl import Workbook  # type: ignore
except Exception:  # pragma: no cover - dependency optional
    Workbook = None


def contest_list(request):
    contests = Contest.objects.all()
    query = request.GET.get('q')
    if query:
        contests = contests.filter(title__icontains=query)
    state = request.GET.get('state')
    if state:
        contests = contests.filter(state__iexact=state)
    return render(request, 'contest_list.html', {'contests': contests})


def export_contests(request):
    """Export contests filtered by query parameters as PDF or Excel."""
    contests = Contest.objects.all()
    query = request.GET.get('q')
    if query:
        contests = contests.filter(title__icontains=query)
    state = request.GET.get('state')
    if state:
        contests = contests.filter(state__iexact=state)

    fmt = request.GET.get('format', 'pdf')

    if fmt == 'excel' and Workbook is not None:
        wb = Workbook()
        ws = wb.active
        ws.append(['Title', 'Organization', 'State', 'Deadline', 'URL'])
        for c in contests:
            ws.append([c.title, c.organization, c.state, c.deadline, c.url])
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)
        response = HttpResponse(
            output.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename="contests.xlsx"'
        return response

    if fmt == 'pdf' and weasyprint is not None:
        html_string = render_to_string('export_pdf.html', {'contests': contests})
        html = weasyprint.HTML(string=html_string)
        pdf_bytes = html.write_pdf()
        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="contests.pdf"'
        return response

    # fallback to plain text listing
    lines = [
        f"{c.title}\t{c.organization}\t{c.state}\t{c.deadline}\t{c.url}" for c in contests
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')
