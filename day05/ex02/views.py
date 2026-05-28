from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import psycopg2
from .forms import resetDataBase

# Create your views here.
def ex02_init(request: HttpRequest) -> HttpResponse:
	try:
		connection = psycopg2.connect(
			dbname="42_bdd",
            user="tgoudman"
			)
		cursor = connection.cursor()

		cursor.execute(""" 
			CREATE TABLE IF NOT EXISTS ex02_movies (
				episode_nb		INTEGER PRIMARY KEY,
				title			VARCHAR(64) UNIQUE NOT NULL,
				opening_crawl	TEXT,
				director		VARCHAR(32) NOT NULL,
				producer		VARCHAR(128) NOT NULL,
				release_date	DATE NOT NULL
				);
		""")
		connection.commit()
		cursor.execute(" SELECT COUNT (*) FROM ex02_movies ")
		countDatabase = cursor.fetchone()[0]
		cursor.close()
		connection.close()
		file = request.path[1:] + ".html"
		return render(request, file, {"database" : countDatabase})
	except psycopg2.OperationalError as e:
		return render(request, "error.html", {"code": "OperationalError", "message": str(e)})
	except psycopg2.ProgrammingError as e:
		return render(request, "error.html", {"code": "ProgrammingError", "message": str(e)})
	except psycopg2.DatabaseError as e:
		return render(request, "error.html", {"code": "DatabaseError", "message": str(e)})
	except Exception as e:
		return render(request, "error.html", {"code": "Error", "message": str(e)})
	
def ex02_populate(request: HttpRequest) -> HttpResponse:
	try:
		connection = psycopg2.connect(
		dbname="42_bdd",
		user="tgoudman"
		)
		cursor = connection.cursor()
		movies = [
			(1, 'The Phantom Menace',		'George Lucas',		'Rick McCallum',									'1999-05-19'),
			(2, 'Attack of the Clones',		'George Lucas',		'Rick McCallum',									'2002-05-16'),
			(3, 'Revenge of the Sith',		'George Lucas',		'Rick McCallum',									'2005-05-19'),
			(4, 'A New Hope',				'George Lucas',		'Gary Kurtz, Rick McCallum',						'1977-05-25'),
			(5, 'The Empire Strikes Back',	'Irvin Kershner',	'Gary Kurtz, Rick McCallum',						'1980-05-17'),
			(6, 'Return of the Jedi',		'Richard Marquand',	'Howard Kazanjian, George Lucas, Rick McCallum', 	'1983-05-25'),
			(7, 'The Force Awakens',		' J. J. Abrams',	'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 		'2015-12-11'),
		]
		form = resetDataBase()
		if request.method == "POST":
			form = resetDataBase(request.POST)
			if form.is_valid():
				cursor.execute("TRUNCATE TABLE ex02_movies;")
		insert_query = """ 
			INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
			VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (episode_nb) DO NOTHING
            RETURNING episode_nb;
			"""
		conflicts = []
		inserted = []
		for movie in movies:
			cursor.execute(insert_query, movie)
			inserted.append(movie)
			if cursor.fetchone() is None:
				conflicts.append(movie[1])
		connection.commit()

		print("Data inserted successfully !")
		cursor.close()
		connection.close()
		file = request.path[1:] + ".html"
		error = ", ".join(conflicts) if conflicts else None
		return render(request, file, {"form": form, "error" : conflicts, "moviesInserted" : inserted})
	except Exception as e:
		return render(request, "error.html", {"code": "Error", "message": str(e)})
		
def ex02_display(request: HttpRequest) -> HttpResponse:
	try:
		connection = psycopg2.connect(
		dbname="42_bdd",
		user="tgoudman"
		)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM ex02_movies;")
		data = cursor.fetchall()
		file = request.path[1:] + ".html"
		if data:
			return render(request, file, {"data": data})
		else:
			return render(request, file, {"error": "No data available"})
	except Exception as e:
		return render(request, file, {"error": "No data available"})

