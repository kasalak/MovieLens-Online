from django.contrib import admin
from .models import Rater, Movie, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'age', 'occupation', 'zipcode']
    pass


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
    pass


class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'stars', 'rater']
    pass


# Register your models here.
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
