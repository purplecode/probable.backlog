from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'list' : [{'x' : 1}, {'x' : 2}]})

def test(request, msg):
    return HttpResponse("Hello, %s. You're at the poll index." % msg)