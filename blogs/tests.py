from django.test import TestCase
from rest_framework import status
from django.urls import reverse
import time

from blogs.models import Category, Post, Comment


def get_post():
    return Post.objects.last()


class CategoryTest(TestCase):

    def setUp(self):
        Category(name='Sample').save()

    def test_get_categories(self):
        start = time.time()
        response = self.client.get(reverse('api-categories'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostTest(TestCase):
    def setUp(self):
        Category(name='Sample').save()
        Post(title='Sample Post', body='Lorem Ipsum').save()

    def test_post_get(self):
        start = time.time()
        response = self.client.get(reverse('api-posts'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_get_by_pk(self):
        start = time.time()
        post_pk = get_post().pk
        response = self.client.get(reverse('api-post-detail', kwargs={'pk': post_pk}), format='json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentTest(TestCase):
    def setUp(self):
        Category(name='Sample').save()
        Post(title='Sample Post', body='Lorem Ipsum').save()
        Comment(author='Unknown', body='Lorem Ipsum', post=get_post()).save()

    def test_comment_post(self):
        post_pk = get_post().pk
        data = {
            'author': 'Pluto',
            'body': 'Dolores',
            'post': post_pk
        }
        start = time.time()
        response = self.client.post(reverse('api-post-comment'), data, format='json',
                                    content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_update(self):
        comment = Comment.objects.last()
        data = {
            'author': 'Pluto',
            'body': 'Dolores',
            'post': comment.post.pk
        }
        start = time.time()
        response = self.client.put(reverse('api-post-comment-detail', kwargs={'pk': comment.pk}), data, format='json',
                                   content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_delete(self):
        comment_pk = Comment.objects.last().pk
        data = [{
            'id': comment_pk
        }]
        start = time.time()
        response = self.client.delete(reverse('api-post-comment'), data, format='json',
                                      content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
