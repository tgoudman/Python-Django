import os
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import NameForm
from datetime import datetime

def secureLogsForm(data: str):
    file_path: Path = settings.EX02_LOG_FILE
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # crée le dossier si nécessaire
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"[{timestamp}] {data}\n")

def ex02Resolver(request: HttpRequest) -> HttpResponse:
    file = f"ex02/{request.path.split('/')[2]}.html"
    if file.find("..") != -1:
        response = render(request, "error.html", {"code": "403", "message": "forbiden"})
        response.status_code = 403
        return response
    try:
        name = None
        if request.method == "POST":
            form = NameForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['your_name']
                secureLogsForm(name)
        else:
            form = NameForm()
        history = []
        log_file = settings.EX02_LOG_FILE
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                history = f.readlines()
            
        return render(request, "ex02/index.html", {"form": form, "history": history, "name": name})
    except TemplateDoesNotExist:
        response  = render(request, "error.html", {"code" : "404", "message" : "file not found" })
    except Exception as e:
        response = render(request, "error.html", {"code" : "500", "message" : e})
        response.status_code = 500
    return response

# Create your views here.
