from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, 'home.html',{})

def contract_view(request,*args, **kwargs):
    return render(request,"contract.html",{})

def social_view(request,*args, **kwargs):
    return HttpResponse("<h1>This is social</h1>")

def about_view(request,*args, **kwargs):
    my_context = {
        "title":"this is about us",
        "my_html":"<h1> Hello World</h1>",
        "this_is_true": True,
        "my_numbers": 1234,
        "my_list": [123,456,789, 'abc']
    }
    return render(request, "about.html",my_context)

#this is only for git checking purpose. nothing to warry about it
