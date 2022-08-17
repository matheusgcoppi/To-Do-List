from django.shortcuts import render

import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        'newyear': now.day == 1 and now.month == 1 #45:00
    })