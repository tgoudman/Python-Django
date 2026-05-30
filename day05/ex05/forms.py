from django import forms
import psycopg2

def get_movies():
    connection = psycopg2.connect(dbname="42_bdd", user="tgoudman")
    cursor = connection.cursor()
    cursor.execute("SELECT episode_nb, title FROM ex05_movies;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return [(row[0], row[1]) for row in data]

class   deleteDatabaseEx05(forms.Form):
    movie = forms.ChoiceField(choices=get_movies)
    movies = forms.BooleanField(label="Delete all data", required=False)