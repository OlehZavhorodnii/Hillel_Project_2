from .views import home, PostDetailView, PostsView, PostDeleteView, PostUpdateView, PostCreateView
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostsView.as_view(), name='list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='detail'),
    path('post_delete/<int:id>/', PostDeleteView.as_view(), name='delete'),
    path('post_update/<int:id>/', PostUpdateView.as_view(), name='update'),
    path('post_create/', PostCreateView.as_view(), name='create')
]
