from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import simondice

urlpatterns = [
    path('',simondice,name='simondice'),
]
