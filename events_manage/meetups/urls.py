from django.urls import path

from . import views
import debug_toolbar
from django.urls import path, include

urlpatterns = [
    path('meetups', views.index, name='all-meetups'),  # domain.com/meetups
    path('meetups/success', views.confirm_registration, name="confirm-registration"),
    path('meetups/<slug:meetup_slug>', views.meetup_detail, name='meetup-detail'),
    path('__debug__/', include(debug_toolbar.urls))
]
