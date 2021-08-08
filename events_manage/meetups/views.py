from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    meetups = [
        {'title': 'A first meetup'},
        {'title': 'A second meetup'}
    ]
    return render(request, 'meetups/index.html', {'show_meetups': True,'meetups': meetups})

