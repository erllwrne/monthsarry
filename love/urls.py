# love/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
    path("letter/<int:letter_id>/", views.letter_view, name="letter"),
]
