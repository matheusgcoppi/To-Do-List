from django.urls import path

from . import views # from the current directory import views

urlpatterns = [
    path("", views.index, name='index'), # when you type /hello it will show up because of the empty string
    path("matheus", views.matheus, name='matheus'),
    path("<str:name>", views.greeting, name="greeting") #any string after slash that I type will activate the function
]