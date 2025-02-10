from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("<h1>Hello, world. You're at the polls page.</h1>")
