from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def hello_world(reques):
    return HttpResponse("<h1>Hello world!</h1>")