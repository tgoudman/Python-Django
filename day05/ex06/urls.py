from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path("init", views.ex06_init),
    path("populate", views.ex06_populate),
    path("display", views.ex06_display),
    path("update", views.ex06_update),
]