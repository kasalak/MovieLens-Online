from django.contrib import admin


class RaterAdmin(admin.ModelAdmin):
    list_display = ['user', 'movies', 'ratings']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'average_rating', 'number of ratings']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rating']

# Register your models here.
# admin.site.register(Rater, RaterAdmin)
# admin.site.register(Movie, MovieAdmin)
# admin.site.register(Rating, RatingAdmin)
