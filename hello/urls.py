
from importlib.resources import path
from unittest.mock import patch

from django.urls import path
urlpatterns = [
    path("", views.index, name='index')
]