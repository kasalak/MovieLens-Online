from django.shortcuts import render
from .models import Movie, Rater, Rating
# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                  'thumbsup/movie_detail.html',
                  {'movie': movie})


def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({
            'movie': rating.movie,
            'stars': '\u2605' * rating.stars,
        })
    return render(request,
                  'thumbsup/rater_detail.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})
