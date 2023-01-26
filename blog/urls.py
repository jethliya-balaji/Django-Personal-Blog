from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('blogs', views.blogs, name="blogsPage"),
    path('blogs/<slug>', views.blogDetail, name="blogDetailPage"),
    path('tags', views.tags, name="tagsPage"),
    path('tags/<slug>', views.blogRelatedToTag, name="blogRelatedToTagPage"),
    path('about', views.about, name="aboutPage"),
]
