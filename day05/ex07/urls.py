from django.urls import re_path, path
from . import views

urlpatterns = [
    path("populate", views.ex07_populate),
    path("display", views.ex07_display),
    path("update", views.ex07_update),
]