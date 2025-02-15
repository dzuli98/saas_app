from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    page_visit_count = page_qs.count
    context = {
        'title': 'My Page',
        'page_visit_count': page_visit_count,
        'total_visits': qs.count()
        }
    path = request.path
    print(path)
    PageVisit.objects.create(path=path)
    return render(request, "home.html", context)