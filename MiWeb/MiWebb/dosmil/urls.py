from django.urls import path
from .views import dosmil
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',dosmil,name='2048'),
]