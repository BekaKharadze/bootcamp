from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Post
from django.views import View

def api_view(request):
    data = {
        "message": "Welcome to the playground",
        "status": "success"
    }
    return JsonResponse(data)

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'core/post_list.html', {'posts': posts})
    

def home_view(request):
    return HttpResponse('idk')