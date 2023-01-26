from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django_extensions.db.fields import AutoSlugField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blogRelatedToTagPage", kwargs={"slug": self.slug})

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(max_length=255)
    body = models.TextField()
    tags = models.ManyToManyField("Tag", verbose_name=_("Tag"), related_name='posts')
    publish = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogDetailPage", kwargs={"slug": self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.name
