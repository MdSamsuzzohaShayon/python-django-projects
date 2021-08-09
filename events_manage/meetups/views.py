from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    meetups = [
        {
            'title': 'A first meetup',
            'location': "USA",
            'slug': 'a-first-meet-up'
        },
        {
            'title': 'A second meetup',
            'location': "Psris",
            'slug': 'second-meet-up'
        }
    ]
    return render(request, 'meetups/index.html', {'show_meetups': True, 'meetups': meetups})
