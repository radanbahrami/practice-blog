from django.urls import path
from .views import post_titles, post_list, post_detail

urlpatterns = [
    path("post-titles/", post_titles, name="post_titles"),
    path("api/posts/", post_list, name="post_list"),
    path("api/posts/<int:pk>/", post_detail, name="post_detail"),
]
