import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template.exceptions import TemplateDoesNotExist

# Create your views here.
def getcolor() -> list[dict] :
    lines = []
    for i in range(50):
        v = int(i * 255 / 49)
        lines.append({
            "black": f"#{v:02X}{v:02X}{v:02X}",
            "green": f"#00{v:02X}00",
            "blue": f"#0000{v:02X}",
            "red": f"#{v:02X}0000"
        })
    return lines

def ex03Resolver(request: HttpRequest) -> HttpResponse:
    try:
        file = f"ex03/{request.path.split('/')[1]}.html"
        if file.find("..") != -1:
            response = render(request, "error.html", {"code": "403", "message": "forbidden"})
            response.status_code = 403
            return response
        lines = getcolor()
        response = render(request, file, {"lines": lines})
    except TemplateDoesNotExist:
            response = render(request, "error.html", {"code": "404", "message": "file not found"})
            response.status_code = 404
    except Exception as e:
            response = render(request, "error.html", {"code": "500", "message": e})
            response.status_code = 500

    return response