from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from helpinghandmain.models import Register
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    context={
        'current_time': current_time
    }
    return render(request,'main/index.html', context=context)

def login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email = email, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {email} !!')
            return redirect('home_detail')
        else:
            messages.info(request, f'account does not exit. Please Register Yourself')
    form = AuthenticationForm()
    return render(request, 'main/login.html')

def register(request):
    return render(request,'main/register.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def home_detail(request):
    return render(request,'main/home_detail.html')
