from django.urls import re_path
from . import views

urlpatterns = [
    re_path("init", views.ex04_init),
]