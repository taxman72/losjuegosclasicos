from django.urls import path
from .views import ahorcado
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',ahorcado,name='ahorcado'),
]