from django.db import models

# Create your models here.
# id is automatic


class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'Did not answer')
    )

    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    zipcode = models.CharField(max_length=5)
    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=40)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=200)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Rating(models.Model):
    stars = models.IntegerField()
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):              # __unicode__ on Python 2
        return '@user {} gives {} a {}'.format(self.user, self.movie, self.stars)


def load_ml_data():
    import csv
    import json

    users = []

    with open('ml-1m/users.dat') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
                                delimiter='\t')

        for row in reader:
            user = {
                'fields': {
                    'gender': row['gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code']
                },
                'model': 'movieDB.Rater',
                'pk': int(row['UserID'])
            }

            users.append(user)

    with open('users.json', 'w') as f:
        f.write(json.dumps(users))


def load_ml_movies():
    import csv
    import json

    movies = []

    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split(
                                    '::'),
                                delimiter='\t')


        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                },
                'model': 'movieDB.Movie',
                'pk': row['MovieID']
            }

            movies.append(movie)

    with open('movies.json' 'w') as f:
        f.write(json.dumps(movies))


def load_ml_ratings():
    import csv
    import json

    ratings = []

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating::Timestamp'.split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'rating': row['Rating'],
                    'movie_id': row['MovieID'],
                    'rater_id': row['UserID'],
                },
                'model': 'movieDB.Ratings',
            }

            ratings.append(rating)

        with open('ratings.json', 'w') as f:
            f.write(json.dumps(ratings))
