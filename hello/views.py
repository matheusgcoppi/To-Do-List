from http.client import HTTP_PORT
import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def matheus(request):
    return HttpResponse("Hello, Matheus")

# def greet(request, name):
#   return HttpResponse(f'Hello, {name.capitalize()}!')   .capitalize is for put the first letter of name in capital 

def greeting(request, name):
    return render(request, "hello/greeting.html", {
        "name": name.capitalize()
    })
    
