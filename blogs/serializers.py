from django.utils import timezone
from rest_framework import serializers

from blogs.models import Category, Post, Comment, CategoryPost


class DeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        category = Category(
            name=validated_data['name']
        )
        category.save()

        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    created_on = serializers.DateTimeField(default=timezone.now, read_only=True)
    last_modified = serializers.DateTimeField(default=timezone.now, read_only=True)

    def create(self, validated_data):
        post = Post(
            title=validated_data['title'],
            body=validated_data['body'],
        )
        post.save()

        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.modified = timezone.now()
        instance.save()

        return instance


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=60)
    body = serializers.CharField()
    created_on = serializers.DateTimeField(default=timezone.now, read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    def create(self, validated_data):
        comment = Comment(
            author=validated_data['author'],
            body=validated_data['body'],
            post=validated_data['post']
        )
        comment.save()

        return comment

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.body = validated_data.get('body', instance.body)
        instance.post = validated_data.get('post', instance.post)
        instance.save()

        return instance


class CategoryPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    def create(self, validated_data):
        category_post = CategoryPost(
            category=validated_data['category'],
            post=validated_data['post']
        )
        category_post.save()

        return category_post

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.post = validated_data.get('post', instance.post)
        instance.save()

        return instance
