from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_titles(request):
    posts = Post.objects.all()
    output = "<br>".join([p.title for p in posts])
    return HttpResponse(output)
