from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("evaluate/", views.evaluate, name="evaluate"),
    path("<int:annotation_id>/save_annotation/'", views.save_annotation, name="save_annotation"),
]