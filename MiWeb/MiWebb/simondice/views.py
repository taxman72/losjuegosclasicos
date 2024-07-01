from django.shortcuts import render


def simondice(request):
    return render(request, 'simondice/simondice.html')
