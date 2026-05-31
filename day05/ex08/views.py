from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import psycopg2

def ex08_init(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        table_planets = """
                CREATE TABLE IF NOT EXISTS ex08_planets(
                id              SERIAL PRIMARY KEY,
                name            VARCHAR(64) UNIQUE NOT NULL,
                climate         TEXT,
                diameter        INT,
                orbital_period  INT,
                population      BIGINT,
                rotation_period INT,
                surface_water   REAL,
                terrain         VARCHAR(128)
                );
                """
        table_people = """
                CREATE TABLE IF NOT EXISTS ex08_people(
                id              SERIAL PRIMARY KEY,
                name            VARCHAR(64) UNIQUE NOT NULL,
                birth_year      VARCHAR(32),
                gender          VARCHAR(32),
                eye_color       VARCHAR(32),
                hair_color      VARCHAR(32),
                height          INT,
                mass            REAL,
                homeworld       VARCHAR(64),
                FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
                );
        """
        connection = psycopg2.connect(dbname="42_bdd", user="tgoudman")
        cursor = connection.cursor()
        cursor.execute(table_planets)
        cursor.execute(table_people)
        connection.commit()
        cursor.close()
        connection.close()
        return render(request, file)
    except Exception as e:
        return render(request, "error.html", {"code": type(e).__name__, "message": str(e)})

def ex08_populate(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        connection = psycopg2.connect(dbname="42_bdd", user="tgoudman")
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE ex08_planets CASCADE;")
        with open('csvFiles/planets.csv') as f:
            resultPlanets = cursor.copy_from(f, 'ex08_planets', sep='\t', null='NULL', columns=(
                'name',
                'climate',
                'diameter',
                'orbital_period',
                'population',
                'rotation_period',
                'surface_water',
                'terrain'
                )
            )
        with open('csvFiles/people.csv') as f:
            resultPeople = cursor.copy_from(f, 'ex08_people', sep='\t', null='NULL', columns=(
                'name',
                'birth_year',
                'gender',
                'eye_color',
                'hair_color',
                'height',
                'mass',
                'homeworld'
                )
            )
        connection.commit()
        cursor.close()
        connection.close()
        return render(request, file, {"resultPeople": resultPeople, "resultPlanets" : resultPlanets})
    except Exception as e:
        return render(request, "error.html", {"message": str(e)})
    
def ex08_display(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + ".html"
        connection = psycopg2.connect(dbname="42_bdd", user="tgoudman")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate
            FROM ex08_people
            JOIN ex08_planets ON ex08_people.homeworld = ex08_planets.name
            WHERE ex08_planets.climate LIKE '%windy%'
            ORDER BY  ex08_people.name ASC;
            """)
        data = cursor.fetchall()
        dataLen = len(data)
        cursor.close()
        connection.close()
        return render(request, file, {"data" : data, "count": dataLen})
    except Exception as e:
        return render(request, "error.html", {"message": str(e)})