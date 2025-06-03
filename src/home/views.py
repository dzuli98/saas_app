from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from visits.models import PageVisit
from django.conf import settings

LOGIN_URL = settings.LOGIN_URL

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
    if request.user.is_authenticated:
        print(request.user.is_authenticated, request.user)
    return render(request, "home.html", context)

VALID_CODE = "1234"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})

@login_required
def user_only_view(request, *args, **kwargs):
    # if not request.user.is_authenticated:
    #     return redirect("/login")
    return render(request, "protected/user-only.html", {})

@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request, "protected/user-only.html", {})