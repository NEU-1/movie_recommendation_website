from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movie_actor', blank=True)
    genres = models.ManyToManyField(Genre, related_name='movie_genre', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=255, null=True, blank=True)

class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)