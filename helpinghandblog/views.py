
from django.shortcuts import render, HttpResponse


def blogindex(request):
    return render(request,'blog/blog.html')


