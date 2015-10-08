from django.shortcuts import render
from django.db.models import Avg

# Create your views here.
def movie_detail(request, movie_id):
    movie = Movie.object.get(pk=movie_id)
    return render(request,
                  'template_name.html',
                  {'movie': movie})

def top_movies(request):

    Movie.objects.annotate(Avg('rating_set.stars'))

    return render(request,
                  'movieDB/top_movies.html',
                  {})
