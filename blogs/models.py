from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)


class CategoryPost(models.Model):
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Post', related_name='category', on_delete=models.SET_NULL, null=True)
