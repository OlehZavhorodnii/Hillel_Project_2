from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, User
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
    queryset = Post.objects.all()
    template_name = 'core/post_update.html'
    pk_url_kwarg = 'id'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts:list')


class PostCreateView(CreateView):
    queryset = Post.objects.all()
    template_name = 'core/post_create.html'
    success_url = reverse_lazy('posts:list')
    form_class = PostForm

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = PostForm(request.POST)
        first_user = form.save(commit=False)
        first_user.user = User.objects.first()
        first_user.save()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
