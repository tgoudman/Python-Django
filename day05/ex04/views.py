from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import psycopg2
import psycopg2.extras

def connectdb() -> psycopg2:
	connection = psycopg2.connect(
	dbname="42_bdd",
	user="tgoudman"
	)
	return connection

def ex04_init(request: HttpRequest) -> HttpResponse:
	try:
		connection = connectdb()
		cursor = connection.cursor()
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS ex04_movies (
				episode_nb		INTEGER PRIMARY KEY,
				title			VARCHAR(64) UNIQUE NOT NULL,
				opening_crawl	TEXT,
				director		VARCHAR(32) NOT NULL,
				producer		VARCHAR(128) NOT NULL,
				release_date	DATE NOT NULL
				);
		""")
		connection.commit()
		cursor.close()
		connection.close()
		file = request.path[1:] + ".html"
		return render(request, file)
	except psycopg2.OperationalError as e:
		return render(request, "error.html", {"code": "OperationalError", "message": str(e)})
	except psycopg2.ProgrammingError as e:
		return render(request, "error.html", {"code": "ProgrammingError", "message": str(e)})
	except psycopg2.DatabaseError as e:
		return render(request, "error.html", {"code": "DatabaseError", "message": str(e)})
	except Exception as e:
		return render(request, "error.html", {"code": "Error", "message": str(e)})

def ex04_populate(request: HttpRequest) -> HttpResponse:
	try:
		file = request.path[1:] + ".html"
		connection = connectdb()
		cursor = connection.cursor()
		movies = [
			(1, 'The Phantom Menace',		'George Lucas',		'Rick McCallum',									'1999-05-19'),
			(2, 'Attack of the Clones',		'George Lucas',		'Rick McCallum',									'2002-05-16'),
			(3, 'Revenge of the Sith',		'George Lucas',		'Rick McCallum',									'2005-05-19'),
			(4, 'A New Hope',				'George Lucas',		'Gary Kurtz, Rick McCallum',						'1977-05-25'),
			(5, 'The Empire Strikes Back',	'Irvin Kershner',	'Gary Kurtz, Rick McCallum',						'1980-05-17'),
			(6, 'Return of the Jedi',		'Richard Marquand',	'Howard Kazanjian, George Lucas, Rick McCallum', 	'1983-05-25'),
			(7, 'The Force Awakens',		'J. J. Abrams',	'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 		'2015-12-11'),
		]

		insert_query = """
			INSERT INTO ex04_movies(episode_nb, title, director, producer, release_date)
			VALUES(%s, %s, %s, %s, %s)
			ON CONFLICT (episode_nb) DO NOTHING
			RETURNING episode_nb;
		"""
		conflicts = []
		inserted = []
		for movie in movies:
			cursor.execute(insert_query, movie)
			if cursor.fetchone() is None:
				print("No data inserted")
				conflicts.append(movie[1])
			else:
				inserted.append(movie)
		connection.commit()
		cursor.close()
		connection.close()
		return render(request, file, {"inserted" : inserted, "conflicts" : conflicts})
	except Exception as e:
		return render(request, "error.html", {"code" : "Error", "message" : str(e)})
	
def ex04_display(request: HttpRequest) -> HttpResponse:
	try:
		file = request.path[1:] + ".html"
		connection = connectdb()
		cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		cursor.execute("SELECT * FROM ex04_movies;")
		data = cursor.fetchall()
		return render(request, file, {"data": data})
	except Exception as e:
		return render(request, "error.html", {"code" : "Error", "message" : str(e)})

def ex04_remove(request: HttpRequest) -> HttpResponse:
	try: 
		file = request.path[1:] + ".html"
		connection = connectdb()
		cursor = connection.cursor()
		cursor.execute(""" DELETE FROM ex04_movies;""")
		connection.commit()
		cursor.close()
		connection.close()
		return render(request, file)
	except Exception as e:
		return render(request, "error.html", {"code" : "Error", "message" : str(e)})
