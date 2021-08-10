from django.urls import path

from . import views
import debug_toolbar
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='all-meetups'),  # domain.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name="confirm-registration"),
    path('<slug:meetup_slug>', views.meetup_detail, name='meetup-detail'),
    path('__debug__/', include(debug_toolbar.urls))
]
