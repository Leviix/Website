from django.shortcuts import render
from django.http import HttpResponse

def Home_page(request):
    return render(request, 'HomePage/Home_Page.html')

def resume(request):
    return render(request, 'HomePage/Resume.html')

def cover(request):
    return render(request, 'HomePage/Cover.html')
