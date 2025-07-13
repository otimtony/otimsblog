# blog/models.py

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from markdown import markdown
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    slug = models.SlugField(unique=True, blank=True)  # new slug field
    content = MarkdownxField()
    tags = TaggableManager() 
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_created')
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts_updated')

    def content_as_html(self):
        return markdown(self.content, extensions=["fenced_code", "codehilite"])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Create slug from title
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
