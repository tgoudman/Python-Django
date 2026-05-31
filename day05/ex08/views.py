from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import psycopg2

def ex08_populate(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        # full_clean() forces Django validation before saving to database
        data_movies = [
            (1, 'The Phantom Menace',		'George Lucas',		'Rick McCallum',									'1999-05-19'),
            (2, 'Attack of the Clones',		'George Lucas',		'Rick McCallum',									'2002-05-16'),
            (3, 'Revenge of the Sith',		'George Lucas',		'Rick McCallum',									'2005-05-19'),
            (4, 'A New Hope',				'George Lucas',		'Gary Kurtz, Rick McCallum',						'1977-05-25'),
            (5, 'The Empire Strikes Back',	'Irvin Kershner',	'Gary Kurtz, Rick McCallum',						'1980-05-17'),
            (6, 'Return of the Jedi',		'Richard Marquand',	'Howard Kazanjian, George Lucas, Rick McCallum', 	'1983-05-25'),
            (7, 'The Force Awakens',		'J. J. Abrams',	    'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 		'2015-12-11'),
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
        return render(request, file, {"inserted" : inserted, "conflicts" : conflicts})
    except Exception as e:
        import traceback
        return render(request, "error.html", {
            "code": type(e).__name__,
            "message": traceback.format_exc()

def ex08_remove(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        movies = Movies.objects.all()
        if len(movies) == 0:
            raise Movies.DoesNotExist
        return render(request, file, {})
    except Exception as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})

def ex08_display(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        getMovies = Movies.objects.all().order_by('episode_nb')
        return render(request, file, {"data" : getMovies})
    except Exception as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})

def ex08_update(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        form = updateDatabase()
        empty = len(get_movies()) == 0
        if (request.method == 'POST'):
            form = updateDatabase(request.POST)
            if form.is_valid():
                opening_crawl = form.cleaned_data["movie"]
                episode = form.cleaned_data["movieSelected"]
                Movies.objects.filter(episode_nb=episode).update(opening_crawl=opening_crawl)
                form = updateDatabase()
                empty = len(get_movies()) == 0
        return render(request, file, {"form": form, "empty": empty})
    except Exception as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})