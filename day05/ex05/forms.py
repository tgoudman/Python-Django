from django import forms
from .models import Movies

def get_movies():
    return list(Movies.objects.values_list('episode_nb', 'title').order_by('episode_nb'))

class deleteDatabaseEx05(forms.Form):
    movie = forms.ChoiceField(choices=get_movies)