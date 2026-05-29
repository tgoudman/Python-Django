from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path("init", views.ex04_init),
    path("populate", views.ex04_populate),
    path("display", views.ex04_display),
    path("remove", views.ex04_remove),
]