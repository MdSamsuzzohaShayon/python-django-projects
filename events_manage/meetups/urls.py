from django.urls import path

from . import views
import debug_toolbar
from django.urls import path, include


urlpatterns = [
    path('meetups', views.index), #domain.com/meetups
    path('__debug__/', include(debug_toolbar.urls))
]


