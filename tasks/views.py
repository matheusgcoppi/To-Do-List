from django.shortcuts import render
import datetime

tasks = ['foo', 'bar', 'baz']

def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })

def add(request):
    return render(request, 'tasks/add.html', {
        # 106
    })