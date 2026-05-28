from django.urls import re_path
from . import views

urlpatterns = [
    re_path("init", views.ex03_init),
    re_path("display", views.ex03_display),
    re_path("delete", views.ex03_delete),
]