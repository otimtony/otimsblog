# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Category
from datetime import datetime
from django.core.paginator import Paginator

def blog_list(request):
    post_list = BlogPost.objects.all().order_by('-created')
    paginator = Paginator(post_list, 12) 

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, 'blog/blog_list.html', {
        'posts': posts, 
        'year': datetime.now().year,
        'categories': categories,
        })

def blog_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = BlogPost.objects.filter(category=category).order_by('-created')
    categories = Category.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': category,
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})
