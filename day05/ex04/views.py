from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import psycopg2

# Create your views here.
def ex04_init(request: HttpRequest) -> HttpResponse:
    try:
        connection = psycopg2.connect(
            dbname="42_bdd",
            user="tgoudman"
        )
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
        file = request.path[1.] + ".html"
        return render(request, file)
    except Exception as e:
        return render(request, "error.html", {'code' : "Error", "message": str(e)})