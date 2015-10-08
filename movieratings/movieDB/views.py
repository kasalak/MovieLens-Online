from django.shortcuts import render

# Create your views here.
def movie_detail(request, movie_id):
    movie = Movie.object.get(pk=movie_id)
    return render(request,
                  'template_name.html',
                  {'movie': movie})
