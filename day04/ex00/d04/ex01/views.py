import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template.exceptions import TemplateDoesNotExist

# Create your views here.
def ex01Reslver(request: HttpRequest) -> HttpResponse:
    file = f"ex01/{request.path.split('/')[2]}.html"
    if file.find("..") != -1:
        response = render(request, "error.html", {"code": "403", "message": "forbidden"})
        response.status_code = 403
        return response
    try:
        context = {
            'fruits' : ['Apple', 'Banana', 'Cherry'],
            'show_message': True,
            'page_title' : 'Engine of template Django',
        }
        response = render(request, file, context)
    except TemplateDoesNotExist:
            response = render(request, "error.html", {"code": "404", "message": "file not found"})
            response.status_code = 404
    except Exception as e:
            response = render(request, "error.html", {"code": "500", "message": e})
            response.status_code = 500


    return response