from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='sections'),
    path('<str:blog_id>', views.blogPost, name='blog-post'),
    path('<str:project_id>', views.projectDetails, name='project-detail'),
]