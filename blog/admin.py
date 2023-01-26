from django.contrib import admin
from .models import Tag, Post, Comment
# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = Comment
    readonly_fields = ['name','email','body']
    can_delete = False
    extra = 0
    raw_id_fields = ['post']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = ['title', 'slug', 'created_at', 'updated_at', 'publish']
    list_filter = ['publish', 'tags', 'created_at']
    inlines = [CommentItemInline]

    class Media:
        js = ("js/tinymce.js",)
