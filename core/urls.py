
from core import views
from .views import PostDetailView, PostsView, PostDeleteView
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostsView.as_view(), name='list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='detail'),
    path('post_delete/<int:id>/', PostDeleteView.as_view(), name='delete')
]
