from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from helpinghandhome.models import usernew
from django.contrib.auth.decorators import login_required

from datetime import datetime
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout



def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    context={
        'current_time': current_time
    }
    return render(request,'main/index.html', context=context)

def login_user(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username = email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,"You Sucessfully Loged In")
            
        else:
            messages.info(request,"account does not exit. Please Register Yourself")
        return redirect('home_detail')
    else:
        return render(request, 'main/login_user.html')

def register(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        signupname = request.POST['signupname']
        signupemail = request.POST['signupemail']
        signuppass1 = request.POST['signuppass1']
        signuppass2 = request.POST['signuppass2']
        
        # signupstate = request.POST.get('signupstate')
        
        # signupsupplier = request.POST.get('signupsupplier')
        if signuppass1==signuppass2:
            try:
                user=User.objects.get(username=signupname)
                messages.error(request, "You already have your account")
            except User.DoesNotExist:
                user = User.objects.create_user(username=signupname,password=signuppass1, email=signupemail)
    
                signupaddress = request.POST['signupaddress']
                signupcontact = request.POST['signupcontact']
                signupcity = request.POST['signupcity']
                signupzip = request.POST['signupzip']
                
                newExtendeduser=usernew(address=signupaddress, contact=signupcontact, city=signupcity, pincode=signupzip)
                
                newExtendeduser.save()
                login(request,user)
                messages.success(request, "You Sucessfully created your account")
                
        else:
            messages.error(request, "Your Password Don't Match")
        return redirect('/home_detail')
    else:
        return render(request, 'main/register.html')
    
    

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/login/')
def home_detail(request):
   
    datas = usernew.objects.filter(user = request.user)
    
    return render(request,'main/home_detail.html', {'data': datas} )
@login_required(login_url='/login/')
def food_details(request):
    return render(request,'main/food_details.html')
@login_required(login_url='/login/')
def user_profile(request):
    return render(request,'main/user_profile.html')
@login_required(login_url='/login/')
def supplier_dashboard(request):
    return render(request,'main/supplier_dashboard.html')
