from django.contrib import admin

from ticketing.models import Movie, Cinema, ShowTime

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(ShowTime)
