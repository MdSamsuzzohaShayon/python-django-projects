from django.contrib import admin
from .models import Meetup

# Register your models here.


# GETTING TWO COLUMNS IN ADMIN MEETUPS
class MeetupAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',) # MAKE A FILTER ON THE RIGHT
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)