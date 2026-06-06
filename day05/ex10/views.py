from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .form import searchForm
from .models import Movies

def ex10_display(request: HttpRequest) -> HttpResponse:
    try:
        file = request.path[1:] + "index.html"
        form = searchForm()
        results = None

        if request.method == "POST":
            form = searchForm(request.POST)
            if form.is_valid():
                minDate  = form.cleaned_data["movieMinDate"]
                maxDate  = form.cleaned_data["movieMaxDate"]
                diameter = form.cleaned_data["planetDiameter"]
                gender   = form.cleaned_data["characterGender"]

                results = Movies.objects.filter(
                    release_date__gte=minDate,
                    release_date__lte=maxDate,
                    characters__gender=gender,
                    characters__homeworld__diameter__gte=diameter
                ).values(
                    'title',
                    'characters__name',
                    'characters__gender',
                    'characters__homeworld__name',
                    'characters__homeworld__diameter'
                ).order_by('title')

        return render(request, file, {"form": form, "results": results})

    except Exception as e:
        return render(request, "error.html", {"code": "Error", "message": str(e)})