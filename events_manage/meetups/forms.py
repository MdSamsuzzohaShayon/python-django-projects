from django import forms
from .models import Participant

# THIS WILL NOT EFFECT ON DATABASE - SINCE WE ARE NO LONGER USING SAVE METHOD SO INSTEAD OF FORM MODEL WE COULD USE REGULAR FORM
class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email', widget=forms.EmailInput(attrs={'class': 'ui segment teal'}))
    # email['subject'].label_tag(attrs={'class': 'foo'})
    
