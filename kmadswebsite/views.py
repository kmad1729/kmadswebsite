from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("hello world")

def my_view(request):
    return render(request, 'about_me.html')
