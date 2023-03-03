from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="blog_home"),
    path('user/<str:username>', views.UserPostList.as_view(), name='user_posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/new/', views.PostCreate.as_view(), name='post_create'),
    path('update/<slug:slug>/', views.PostUpdate.as_view(), name='post_update'),
    path('delete/<slug:slug>/', views.PostDelete.as_view(), name='post_delete'),
]
