from django.shortcuts import render

from ticketing.models import Movie, Cinema


def movie_list(request):
    # 1- selecting data
    movies = Movie.objects.all()
    # 2- some code like authentications
    # 3- render responses
    context = {
        'movies': movies,
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    # 1- selecting data
    cinemas = Cinema.objects.all()
    # 2- some code like authentications
    # 3- render responses
    context = {
        'cinemas': cinemas,
    }
    return render(request, 'ticketing/cinema_list.html', context)
