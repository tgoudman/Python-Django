from django.urls import re_path
from . import views

urlpatterns = [
    re_path("populate", views.ex03_populate),
    re_path("display", views.ex03_display),
    re_path("delete", views.ex03_delete),
]