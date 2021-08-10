from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm


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
        if request.method == "GET":
            registration_form = RegistrationForm()
            return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                # 'meetup_title': selected_meetup.title,
                # 'meetup_description' : selected_meetup.description
                'meetup': selected_meetup,
                'form': registration_form
            })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ =  Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
                
    except Exception as e:
        print(e)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
    
def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')
