from django.urls import path
# from .views import PostListView, PostDetailView
from django.conf.urls.static import static
from . import views
from .models import Post

app_name = "application" 

urlpatterns = [
    # path('', views.index),
    path('', views.PostListView.as_view(), name='home-page'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(model=Post, success_url='/'), name='create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(model=Post, success_url='/'), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(model=Post, success_url='/'), name='post_delete'),
    path('aboutus/', views.aboutUs),
]

