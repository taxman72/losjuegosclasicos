# tictactoe/urls.py

from django.urls import path
from .views import snake
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',snake,name='snake'),
]
