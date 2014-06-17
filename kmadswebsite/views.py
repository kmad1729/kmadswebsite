from django.http import HttpResponse
from django.shortcuts import render

from kmadswebsite.models import MyBook, MyMovie
from datetime import datetime

def home(request):
    return HttpResponse("hello world")

def index_view(request):
    page_info_dict = {}
    page_info_dict["my_books"] = MyBook.objects.order_by("-read_date")

    page_info_dict["my_movies"] = MyMovie.objects.order_by("-watch_date")

    page_info_dict["server_date"] = datetime.now()

    return render(request, 'about_me.html', page_info_dict)
