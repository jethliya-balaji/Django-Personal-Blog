from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView, CommentCreateAPIView
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('blogs/', PostListCreateAPIView.as_view()),
    path('blog/<slug:slug>/', PostRetrieveUpdateDestroyAPIView.as_view()), 
    path('tags/', TagListCreateAPIView.as_view()),
    path('tag/<slug:slug>/', TagRetrieveUpdateDestroyAPIView.as_view()), 
    path('comment/', CommentCreateAPIView.as_view()),
]
