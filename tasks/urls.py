from nturl2path import url2pathname
from django.urls import path
from . import views

app_name = 'tasks' # I create it to be more specify

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = 'add') # When I say to django link some url is with the name 
]