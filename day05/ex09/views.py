from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Planets, People
import psycopg2

def ex09_display(request: HttpRequest) -> HttpResponse:
    try:
        connection = psycopg2.connect(dbname="42_bdd", user="tgoudman")
        cursor = connection.cursor()
        file = request.path[1:] +'.html'
        people = People.objects.filter(
            homeworld__climate__icontains="windy"
        ).order_by("name")
        if not people.exists():
            return HttpResponse(
                "No data available, please use the following command line before use:<br>"
                "python3 manage.py loaddata ex09_initial_data.json"
            )
        return render(request, file, {'data' : people})
    except Exception as e:
        return render(request, "error.html", {"code" : "test", "message" : str(e)})
    
