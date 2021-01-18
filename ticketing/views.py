from django.shortcuts import render

from ticketing.models import Movie, Cinema


def movie_list(request):
    # 1- selecting data
    movies = Movie.objects.all()
    # 2- some code like authentications
    # 3- render responses
    context = {
        'movie_list': movies,
        'count': len(movies),
    }
    return render(request, 'movie_list.html', context)


def cinema_list(request):
    # 1- selecting data
    cinemas = Cinema.objects.all()
    # 2- some code like authentications
    # 3- render responses
    context = {
        'cinema_list': cinemas,
        'count': len(cinemas),
    }
    return render(request, 'cinema_list.html', context)
