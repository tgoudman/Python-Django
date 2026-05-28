from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Movies

def ex03_init(request: HttpRequest) -> HttpResponse:
    file = request.path[1:] + ".html"
    data_movies = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum ", "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kutz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk -", "2015-12-11"),
    ]
    for movie in data_movies:
        try:
            movieClass, created = Movies.objects.get_or_create(
                episode_nb=movie[0],
                defaults={
                    "title": movie[1],
                    "director": movie[2],
                    "producer": movie[3],
                    "release_date": movie[4],
                }
            )
            movieClass.full_clean()
        except Exception as e:
            return render(request, "error.html", {"code": "OperationalError", "message": str(e)})
    return render(request, file)
    
def ex03_display(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        movie = Movies.objects.all()
        return render(request, file, {"movies": movie})
    except Exception as e:
        return render(request, "error.html", {"code" : "", "message" : str(e)})

def ex03_delete(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        movie = Movies.objects.all()
        movie.delete()
        return render(request, file)
    except Exception as e:
        return render(request, "error.html", {"code" : "", "message" : str(e)})