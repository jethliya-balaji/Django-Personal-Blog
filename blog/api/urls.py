from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView, CommentCreateAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('blogs/', PostListCreateAPIView.as_view()),
    path('blog/<slug:slug>', PostRetrieveUpdateDestroyAPIView.as_view()), 
    path('tags/', TagListCreateAPIView.as_view()),
    path('tag/<slug:slug>', TagRetrieveUpdateDestroyAPIView.as_view()), 
    path('comment/', CommentCreateAPIView.as_view()),
    path('auth/', obtain_auth_token),
]
