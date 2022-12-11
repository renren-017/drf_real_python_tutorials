from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
import time
from django.core.files.uploadedfile import SimpleUploadedFile

from blogs.models import Category

User = get_user_model()


def get_user(pk):
    return User.objects.get(pk=pk)


def get_file():
    return SimpleUploadedFile(name='test_image.jpg',
                              content='',
                              content_type='image/jpeg')


class BoardTest(TestCase):

    def setUp(self):
        User(username='n@user.com', password='foo').save()
        User(username='n2@user.com', password='foo').save()
        Category(name='Sample').save()

    def test_get_categories(self):
        user = get_user(1)
        self.client.force_login(user)

        start = time.time()
        response = self.client.get(reverse('api-categories'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_category_create(self):
        user = get_user(1)
        self.client.force_login(user)

        data = {
            'name': 'Sample2'
        }

        start = time.time()
        response = self.client.post(reverse('api-categories'), data, format='json')
        end = time.time()

        self.assertLess(end - start, 0.2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)