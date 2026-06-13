from django.db import models
import datetime

# Create your models here.
class   Planets(models.Model):
    name =              models.CharField(max_length=64, unique=True)
    climate =           models.TextField(null=True)
    diameter =          models.IntegerField(null=True)
    orbital_period =    models.IntegerField(null=True)
    population =        models.BigIntegerField(null=True)
    rotation_period =   models.IntegerField(null=True)
    surface_water =     models.FloatField(null=True, blank=True)
    terrain =           models.TextField(null=True, blank=True)
    created =           models.DateTimeField(default=datetime.datetime.now)
    updated =           models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = "ex10_planets"

    def __str__(self):
        return self.name

class   People(models.Model):
    name =              models.CharField(max_length=64, unique=True)
    birth_year =        models.CharField(max_length=32, null=True, blank=True)
    gender =            models.CharField(max_length=32, null=True, blank=True)
    eye_color =         models.CharField(max_length=32, null=True, blank=True)
    hair_color =        models.CharField(max_length=32, null=True, blank=True)
    height =            models.IntegerField(null=True)
    mass =              models.FloatField(null=True)
    homeworld =         models.ForeignKey('Planets', on_delete=models.CASCADE, null=True, blank=True)
    created =           models.DateTimeField(default=datetime.datetime.now)
    updated =           models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = "ex10_people"

    def __str__(self):
        return self.name


class Movies(models.Model):
    episode_nb    = models.IntegerField(primary_key=True)
    title         = models.CharField(max_length=64, unique=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director      = models.CharField(max_length=32)
    producer      = models.CharField(max_length=128)
    release_date  = models.DateField()
    characters    = models.ManyToManyField(People, blank=True)
    class Meta:
        db_table = "ex10_movies"

    def __str__(self):
        return self.title