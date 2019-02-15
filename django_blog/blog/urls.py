from django.urls import path
from .views import (
    about,
    PostCreateView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-post'),
    #path('posts/', PostListView.as_view(), name='post-list'),

    path('about/', about, name='about'),
]