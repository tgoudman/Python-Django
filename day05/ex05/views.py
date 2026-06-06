from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import psycopg2
import psycopg2.extras
from .models import Movies
from .forms import get_movies, deleteDatabaseEx05

def ex05_populate(request: HttpRequest) -> HttpResponse:
	try:
		file = request.path[1:] + ".html"
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
			movieClass.full_clean()
		return render(request, file, {"inserted" : inserted, "conflicts" : conflicts})
	except Exception as e:
		return render(request, "error.html", {"code" : "Error", "message" : str(e)})
	
def ex05_display(request: HttpRequest) -> HttpResponse:
	try:
		file = request.path[1:] + ".html"
		data = Movies.objects.all()
		return render(request, file, {"data" : data})
	except Exception as e:
		return render(request, "error.html", {"code" : "Error", "message" : str(e)})

def ex05_remove(request: HttpRequest) -> HttpResponse:
	try: 
		file = request.path[1:] + ".html"
		form = deleteDatabaseEx05()
		empty = len(get_movies()) == 0
		if request.method == 'POST':
			form = deleteDatabaseEx05(request.POST)
			if form.is_valid():
				episode = form.cleaned_data["movie"]
				Movies.objects.filter(episode_nb=episode).delete()
				empty = len(get_movies()) == 0
		return render(request, file, {"form": form, "empty": empty})
	except Exception as e:
		return render(request, "error.html", {"code" : "Error", "message" : str(e)})
