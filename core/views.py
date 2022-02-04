from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
    

def home(request):
    return render(request, "core/home.html")


class PostsView(ListView):
    template_name = 'core/posts.html'
    queryset = Post.objects.all()
    