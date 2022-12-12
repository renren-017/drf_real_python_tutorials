from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def categories(self):
        categories_posts = CategoryPost.objects.filter(post=self)
        categories = [cp.category.name for cp in categories_posts]

        return categories


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.body


class CategoryPost(models.Model):
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Post', related_name='category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.post
