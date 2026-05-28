from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Movies
from django.db import models
import psycopg2

# Create your views here.*

def ex01resolver(request: HttpRequest) -> HttpResponse:
	try:
		movies, created = Movies.objects.get_or_create(episode_nb=1, defaults={"title":"Matrix", "opening_crawl":"A hacker discovers the world he lives in is a simulation.", "director":"Lana Wachowski, Lilly Wachowski", "producer":"Joel Silver", "release_date":"1999-03-31",})
		# full_clean() forces Django validation before saving to database
		movies.full_clean()
		movies.save()
	except Exception as e:
		return render(request, "error.html", {"code": "OperationalError", "message": str(e)})
	return render(request, "init01.html", {"movies": movies})