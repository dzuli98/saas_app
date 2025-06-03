from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'auth/login.html', {})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Django forms will handle this
        # user_exists= User.objects.filter(username__iexact=username).exists()
        # email_exists= User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(username, email, password)
        except:
            pass
    return render(request, 'auth/register.html', {})