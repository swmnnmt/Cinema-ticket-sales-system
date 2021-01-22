from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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


def movie_details(request, movie_id):
    # if object exists return it otherwise 404
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie':movie
    }
    return render(request,'ticketing/movie_details.html',context)


def cinema_details(request, cinema_id):
    # if object exists return it otherwise 404
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request,'ticketing/cinema_details.html',context)
