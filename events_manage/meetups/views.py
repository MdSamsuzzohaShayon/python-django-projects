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



# THIS MEET UP SLUG I PASSED IN URL TO GET SOME VALUE FROM URL
# WHAT EVER WE PASS AFTER http://localhost:8000/meetups/a-first-meetup WE WILL GET VALUE LIKE A-FIRST-MEETUP
def meetup_detail(request, meetup_slug):
    # print(meetup_slug)
    selected_meetup = {
        'title': "First meet up",
        'description': 'This is first meet up descriptions'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description' : selected_meetup['description']
    })
