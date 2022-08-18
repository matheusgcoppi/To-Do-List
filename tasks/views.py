from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "tasks/index.html", {
        'newyear': now.day == 18 and now.month == 8 
    })