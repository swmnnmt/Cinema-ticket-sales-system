from django.urls import path

from ticketing import views

urlpatterns = [
    path('movie/list', views.movie_list, name='movie_list'),
    path('cinema/list', views.cinema_list, name='cinema_list'),
]
