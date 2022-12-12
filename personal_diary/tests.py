from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
import time

from personal_diary.models import Entry


def get_entry():
    return Entry.objects.last()


class EntryTest(TestCase):
    def setUp(self):
        Entry(title='Sample', content='something').save()
        User(username='noname', email='noname@gmail.com', password='blabla1234').save()
        user = User.objects.last()
        user.is_staff = True
        user.is_admin = True
        user.save()


    def test_entries_get(self):
        user = User.objects.last()
        self.client.force_login(user)

        start = time.time()
        response = self.client.get(reverse('api-entries'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.05)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_entries_get_by_pk(self):
        user = User.objects.last()
        self.client.force_login(user)

        start = time.time()
        response = self.client.get(reverse('api-entry-detail', kwargs={'pk': get_entry().pk}), format='json')
        end = time.time()

        self.assertLess(end - start, 0.05)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_entries_post(self):
        data = {
            'title': 'Sample 2',
            'content': 'Description 2'
        }
        user = User.objects.last()
        self.client.force_login(user)

        start = time.time()
        response = self.client.post(reverse('api-entries'), data, format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_entry_update(self):
        user = User.objects.last()
        self.client.force_login(user)

        data = {
            'title': 'Sample 2 Upd',
            'content': 'Description 2 Upd',
        }
        start = time.time()
        response = self.client.put(reverse('api-entry-detail', kwargs={'pk': get_entry().pk}),
                                   data, format='json', content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_entry_delete(self):
        user = User.objects.last()
        self.client.force_login(user)

        start = time.time()
        response = self.client.delete(reverse('api-entry-detail', kwargs={'pk': get_entry().pk}),
                                      format='json', content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
