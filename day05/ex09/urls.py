from django.urls import re_path, path
from . import views

urlpatterns = [
    path("display", views.ex09_display)
]