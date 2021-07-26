from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def calculate():
    x =10
    y= 20
    return x+y

def say_hi(request):
    x = calculate()
    return render(request, "hello.html", {'name': 'Neymar JR'})