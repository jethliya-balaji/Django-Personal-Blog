from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.db.models import Count
from .models import Tag, Post
from .forms import CommentForm
from .utils import paginate

# Create your views here.

def home(request):
    posts = Post.objects.filter(publish=True)[:4]
    return render(request, 'blog/home.html', {'posts':posts})

def blogs(request):
    posts = Post.objects.filter(publish=True)

    query =''
    if 'query' in request.GET:
        query = request.GET['query']
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(tags__name__icontains=query)).distinct()

    posts = paginate(request, posts, 6)
    return render(request, 'blog/blogs.html', {'posts':posts, 'query':query})

def blogDetail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    previous_post = Post.objects.filter(created_at__lt=blog.created_at, publish=True).order_by('-created_at').first()
    next_post = Post.objects.filter(created_at__gt=blog.created_at, publish=True).order_by('created_at').first()

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = blog
        comment.save()
        return redirect('blogDetailPage', slug=blog.slug)

    return render(request, 'blog/blog_detail.html', {'blog':blog, 'previous_post':previous_post, 'next_post':next_post, 'form':form})

def tags(request):
    tags = Tag.objects.annotate(post_count=Count('posts', filter=Q(posts__publish=True)))
    return render(request, 'blog/tags.html', {'tags':tags})

def blogRelatedToTag(request, slug):
    tags = Tag.objects.annotate(post_count=Count('posts', filter=Q(posts__publish=True)))
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, publish=True)
    posts = paginate(request, posts, 6)
    return render(request, 'blog/blogs_related_to_tag.html', {'tags':tags, 'tag':tag, 'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

def custom_404(request, exception):
    return render(request, '404.html')
