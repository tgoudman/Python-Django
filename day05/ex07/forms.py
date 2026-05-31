from django import forms
from .models import Movies

import psycopg2

def get_movies():
    return list(Movies.objects.values_list('episode_nb', 'title').order_by('episode_nb'))

class   updateDatabase(forms.Form):
    movie = forms.CharField(widget=forms.Textarea())
    movieSelected = forms.ChoiceField(choices=get_movies)

