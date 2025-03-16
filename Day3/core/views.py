from django.shortcuts import render
from core.models import Post
post = Post.objects.get(id=1)

comments = post.comments.all()
