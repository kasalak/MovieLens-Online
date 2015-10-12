from django.shortcuts import render

# Create your views here.


def movie_detail(request, movie_ID):
    movie = Movie.objects.get(pk=movie_ID)
    return render(request,
                  'template_name.html',
                  {'movie': movie})
