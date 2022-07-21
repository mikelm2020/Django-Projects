# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgeRatings(models.Model):
    age_rating = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'age_ratings'


class FilmGenders(models.Model):
    movie_gender = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'film_genders'


class OriginCountries(models.Model):
    origin_country = models.CharField(max_length=50)
    iso_code = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'origin_countries'


class StreamingServices(models.Model):
    streaming_service = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'streaming_services'


class Users(models.Model):
    login = models.CharField(max_length=10)
    pass_field = models.CharField(db_column='pass', max_length=10)  # Field renamed because it was a Python reserved word.
    user_name = models.CharField(max_length=30)
    active = models.BooleanField

    class Meta:
        managed = False
        db_table = 'users'


class Movies(models.Model):
    movie_name = models.CharField(max_length=150)
    duration = models.IntegerField(blank=True, null=True)
    movie_year = models.IntegerField()
    age_rating = models.ForeignKey(AgeRatings, models.DO_NOTHING)
    active = models.BooleanField

    class Meta:
        managed = False
        db_table = 'movies'


class MovieCountries(models.Model):
    movie = models.ForeignKey('Movies', models.DO_NOTHING)
    country = models.ForeignKey('OriginCountries', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_countries'


class MovieGenders(models.Model):
    movie = models.ForeignKey('Movies', models.DO_NOTHING)
    film_gender = models.ForeignKey(FilmGenders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_genders'


class MoviesStreamings(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    streaming = models.ForeignKey('StreamingServices', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_streamings'


class Series(models.Model):
    serie_name = models.CharField(max_length=150)
    seasons = models.SmallIntegerField()
    serie_year = models.IntegerField()
    age_rating = models.ForeignKey(AgeRatings, models.DO_NOTHING)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'series'


class SerieCountries(models.Model):
    serie = models.ForeignKey('Series', models.DO_NOTHING)
    country = models.ForeignKey(OriginCountries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'serie_countries'


class SerieGenders(models.Model):
    serie = models.ForeignKey('Series', models.DO_NOTHING)
    film_gender = models.ForeignKey(FilmGenders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'serie_genders'


class SeriesStreamings(models.Model):
    serie = models.ForeignKey(Series, models.DO_NOTHING)
    streaming = models.ForeignKey('StreamingServices', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'series_streamings'


class UserMovies(models.Model):
    movie_viewed = models.IntegerField()
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_movies'


class UserSeries(models.Model):
    serie = models.ForeignKey(Series, models.DO_NOTHING)
    serie_viewed = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_series'



