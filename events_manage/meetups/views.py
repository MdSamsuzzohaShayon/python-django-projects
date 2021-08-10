from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup


# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups': meetups})



# THIS MEET UP SLUG I PASSED IN URL FILE TO GET SOME VALUE FROM URL
# WHAT EVER WE PASS AFTER http://localhost:8000/meetups/a-first-meetup WE WILL GET VALUE LIKE A-FIRST-MEETUP
def meetup_detail(request, meetup_slug):
    # print(meetup_slug)
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            # 'meetup_title': selected_meetup.title,
            # 'meetup_description' : selected_meetup.description
            'meetup': selected_meetup
        })
    except:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
