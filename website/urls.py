from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='sections'),
    path('blogs/<str:blog_id>', views.blogPost, name='blog-post'),
    path('projects/<str:project_id>', views.projectDetails, name='project-detail'),
]