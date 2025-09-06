from django.urls import path
from .views import post_titles

urlpatterns = [
    path("post-titles/", post_titles, name="post_titles")
]