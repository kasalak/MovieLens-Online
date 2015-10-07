from django.db import models

# Create your models here.
class Rater(models.Model):
    rater = models.IntegerField()
    #return self.rater_text
class Movie(models.Model):
    movie = models.CharField(max_length=200)

    #def __str__(self):              # __unicode__ on Python 2
        #return self.movie_text
class Rating(models.Model):
    rating = models.IntegerField()
    #def __str__(self):              # __unicode__ on Python 2
        #return self.rating_text
