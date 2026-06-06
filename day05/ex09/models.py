from django.db import models

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
    created =           models.DateTimeField(auto_now_add=True)
    updated =           models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ex09_planets"

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
    created =           models.DateTimeField(auto_now_add=True)
    updated =           models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ex09_people"

    def __str__(self):
        return self.name