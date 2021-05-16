from django.shortcuts import render, HttpResponse
# from bimbodesigner.models import Feedback, Contact
# from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'main/index.html')


