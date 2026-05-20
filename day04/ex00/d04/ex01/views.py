import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
def ex01Reslver(request: HttpRequest) -> HttpResponse:
    file = f"ex01/{request.path.split('/')[2]}.html"
    print("DBUG: " + file)
    if file.find("..") != -1:
        response = render(request, "error.html", {"code": "403", "message": "forbidden"})
        response.status_code = 403
        return response
    try:
        response = render(request, file)
    except:
        response = render(request, "error.html", {"code": "404", "message": "file not found"})
        response.status_code = 404

    return response