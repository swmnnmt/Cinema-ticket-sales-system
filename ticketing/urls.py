from django.urls import path

from ticketing import views

urlpatterns = [
    path('movie/list/', views.movie_list, name='movie_list'),
    path('cinema/list/', views.cinema_list, name='cinema_list'),
    path('movie/details/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('cinema/details/<int:cinema_id>/', views.cinema_details, name='cinema_details'),
]
