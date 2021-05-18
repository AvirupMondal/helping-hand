from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from helpinghandmain.models import Register
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
  
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        if user is not None:
            form = login(request, user)
            messages.success("You Sucessfully Loged In")
            return redirect('home_detail')
        else:
            messages.info("account does not exit. Please Register Yourself")
    
    return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        signupname = request.POST['signupname']
        signupemail = request.POST['signupemail']
        signuppass1 = request.POST['signuppass1']
        signuppass2 = request.POST['signuppass2']
        signupaddress = request.POST['signupaddress']
        signupcontact = request.POST['signupcontact']
        signupcity = request.POST['signupcity']
        signupstate = request.POST['signupstate']
        signupzip = request.POST['signupzip']
        signupsupplier = request.POST['signupsupplier']
        user = User.objects.create_user(signupname,signupemail,signuppass1,signupaddress,signupcontact, signupcity,signupstate,signupzip,signupsupplier)
        user.save()
        messages.success(request, "You Sucessfully created your account")
        return redirect('home_detail')
    else:
        return render(request, 'main/register.html')
    
    

def logout_view(request):
    logout(request)
    return redirect('index')


def home_detail(request):
    return render(request,'main/home_detail.html')

def food_details(request):
    return render(request,'main/food_details.html')

def user_profile(request):
    return render(request,'main/user_profile.html')

def supplier_dashboard(request):
    return render(request,'main/supplier_dashboard.html')
