from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random"),
    path("new", views.new, name="new"),
    path("wiki/<str:name>/edit", views.edit, name="edit"),
]
