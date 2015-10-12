from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'movie/(?P<movie_id>\d+)$', views.movie_detail),
]
