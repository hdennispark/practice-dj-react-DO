from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#this page is a request handler
# action..?

def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Dennis'})
