from django.urls import re_path, path
from . import views

urlpatterns = [
    path("init", views.ex08_init),
    path("populate", views.ex08_populate),
   path("display", views.ex08_display),
]