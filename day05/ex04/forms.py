from django import forms
import psycopg2

def get_movies():
    connection = psycopg2.connect(dbname="42_bdd", user="tgoudman")
    cursor = connection.cursor()
    cursor.execute("SELECT episode_nb, title FROM ex04_movies LIMIT 10;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return [(row[0], row[1]) for row in data]

class   deleteDatabaseEx04(forms.Form):
    movie = forms.ChoiceField(choices=get_movies)
    movies = forms.BooleanField(label="Delete all data", required=False)