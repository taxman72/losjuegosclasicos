# views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse

def snake(request):
    return render(request, 'snake/snake.html')

