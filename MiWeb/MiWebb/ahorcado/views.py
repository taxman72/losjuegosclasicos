from django.shortcuts import render
from django.http import HttpResponse

def ahorcado(request):
    return render(request, 'ahorcado/ahorcado.html')
