from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy


def home(request):
    return render(request, "core/home.html")


class PostsView(ListView):
    template_name = 'core/posts.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        results = [
            (
                p,
                p.like_set.filter(status=True).count(),
                p.like_set.filter(status=False).count
            )
            for p in posts
        ]

        ctx['results'] = results

        return ctx


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'core/post.html'
    pk_url_kwarg = 'id'


class PostDeleteView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'core/post_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('posts:list')


class PostUpdateView(UpdateView):
    pass


class PostCreateView(CreateView):
    pass
