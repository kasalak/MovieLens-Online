from django.db import models


# Create your models here.
class Rater(models.Model):
    male = 'M'
    female = 'F'
    gender_choices = [(male, 'Male'), (female, 'Female')]
    gender = models.CharField(max_length=1, choices=gender_choices)
    zipcode = models.CharField(max_length=5)
    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return "rater ID {}".format(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=200)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return self.title


class Rating(models.Model):
    stars = models.IntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return '@rater {} gives {} a {}'.format(self.rater, self.movie,
                                                self.stars)


def load_all_ml_data():
    import csv
    import json

    raters = []

    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='RaterID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            rater = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'thumbsup.Rater',
                'pk': int(row['RaterID']),
            }

            raters.append(rater)

    with open('raters.json', 'w') as f:
        f.write(json.dumps(raters))

        movies = []

    with open('ml-1m/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split(
                                '::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title']
                },
                'model': 'thumbsup.Movie',
                'pk': row['MovieID']
            }

            movies.append(movie)

            with open('movies.json', 'w') as f:
                f.write(json.dumps(movies))

    ratings = []

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='RaterID::MovieID::Rating'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'stars': row['Rating'],
                    'rater': row['RaterID'],
                    'movie': row['MovieID']
                },
                'model': 'thumbsup.Rating',
            }

            ratings.append(rating)

    with open('ratings.json', 'w') as f:
        f.write(json.dumps(ratings))
