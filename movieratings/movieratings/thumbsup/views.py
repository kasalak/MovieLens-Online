from django.shortcuts import render
from .models import Movie, Rater, Rating
# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # ratings = movie.ratings_set.all()
    # user_ratings= []
    
    return render(request,
                  'thumbsup/movie_detail.html',
                  {'movie': movie})
