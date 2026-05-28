from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import psycopg2

def connectDataBase(request):
    # Connect to an existing database
    try:
        conn = psycopg2.connect(
            dbname="42_bdd",
            user="tgoudman"
        )
        # Open a cursor to perform database operations
        cur = conn.cursor()
        # Create a new TABLE
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
                episode_nb      INTEGER PRIMARY KEY,
                title           VARCHAR(64) UNIQUE NOT NULL,
                opening_crawl   TEXT,
                director        VARCHAR(32) NOT NULL,
                producer        VARCHAR(128) NOT NULL,
                release_date    DATE NOT NULL
                );
        """)
        # Make the changes to the database persistent
        conn.commit()
        # Close cursor
        cur.close()
        # close connection
        conn.close()
        return None
    except psycopg2.OperationalError as e:
        return render(request, "error.html", {"code": "OperationalError", "message": str(e)})
    except psycopg2.ProgrammingError as e:
        return render(request, "error.html", {"code": "ProgrammingError", "message": str(e)})
    except psycopg2.DatabaseError as e:
        return render(request, "error.html", {"code": "DatabaseError", "message": str(e)})
    except Exception as e:
        return render(request, "error.html", {"code": "Error", "message": str(e)})
    
def ex00resolver(request: HttpRequest) -> HttpResponse:
    file = f"{request.path.split('/')}"
    if file.find("..") != -1:
        print("Invalid request")
    error = connectDataBase(request)
    if error:
        return error
    return render(request, "init.html")
    