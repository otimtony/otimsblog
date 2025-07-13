from django.contrib import admin
from .models import BlogPost, Category
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(BlogPost, MarkdownxModelAdmin)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created')
    list_filter = ('category', 'created')
    search_fields = ('title', 'summary', 'content', 'tags')
    ordering = ('-created',)
    readonly_fields = ('created',)

    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'content', 'tags', 'category', 'author')
        }),
        ('Metadata', {
            'fields': ('created',),
            'classes': ('collapse',),
        }),
    )
