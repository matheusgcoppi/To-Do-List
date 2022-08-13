from http.client import HTTPResponse
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello world');
