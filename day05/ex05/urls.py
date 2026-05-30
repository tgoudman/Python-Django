from django.urls import re_path, path
from . import views

urlpatterns = [
    path("populate", views.ex05_populate),
    path("display", views.ex05_display),
    path("remove", views.ex05_remove),
]