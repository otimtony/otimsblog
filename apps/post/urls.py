# blog/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:category_slug>/', views.blog_list_by_category, name='blog_list_by_category'),
]
