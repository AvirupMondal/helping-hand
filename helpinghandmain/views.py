from django.shortcuts import render, HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    context={
        'current_time': current_time
    }
    return render(request,'main/index.html', context=context)


