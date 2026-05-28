from django.urls import re_path
from . import views

urlpatterns = [
    re_path("init", views.ex02_init),
    re_path("populate", views.ex02_populate),
    re_path("display", views.ex02_display)
]