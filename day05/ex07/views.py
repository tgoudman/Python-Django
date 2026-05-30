from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Movies
from django.db import models
import psycopg2


def ex07_populate(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        movies, created = Movies.objects.get_or_create(episode_nb=1, defaults={"title":"Matrix", "opening_crawl":"A hacker discovers the world he lives in is a simulation.", "director":"Lana Wachowski, Lilly Wachowski", "producer":"Joel Silver", "release_date":"1999-03-31",})
        # full_clean() forces Django validation before saving to database
        data_movies = [
            (1, 'The Phantom Menace',		'George Lucas',		'Rick McCallum',									'1999-05-19'),
            (2, 'Attack of the Clones',		'George Lucas',		'Rick McCallum',									'2002-05-16'),
            (3, 'Revenge of the Sith',		'George Lucas',		'Rick McCallum',									'2005-05-19'),
            (4, 'A New Hope',				'George Lucas',		'Gary Kurtz, Rick McCallum',						'1977-05-25'),
            (5, 'The Empire Strikes Back',	'Irvin Kershner',	'Gary Kurtz, Rick McCallum',						'1980-05-17'),
            (6, 'Return of the Jedi',		'Richard Marquand',	'Howard Kazanjian, George Lucas, Rick McCallum', 	'1983-05-25'),
            (7, 'The Force Awakens',		'J. J. Abrams',	'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 		'2015-12-11'),
        ]
        conflicts = []
        inserted = []
        for movie in data_movies:
            movieClass, created = Movies.objects.get_or_create(
                episode_nb=movie[0],
                defaults={
                    "title"			: movie[1],
                    "director"		: movie[2],
                    "producer"		: movie[3],
                    "release_date"	: movie[4],
                }
            )
            if created:
                inserted.append(movie[1])
            else:
                conflicts.append(movie[1])
            movies.full_clean()
            movies.save()
        return render(request, file, {"inserted" : inserted, "conflicts" : conflicts})
    except Exception as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})

def ex07_remove(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        movies = Movies.objects.all()
        if len(movies) == 0:
            raise Movies.DoesNotExist
        return render(request, file, {"inserted" : inserted, "conflicts" : conflicts})
    except Exception as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})

def ex07_display(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        return render(request, file, {"inserted" : inserted, "conflicts" : conflicts})
    except Exception as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})

def ex07_update(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        return render(request, file, {"inserted" : inserted, "conflicts" : conflicts})
    except Exception as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})