from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from django.urls import reverse
import time

from content_aggregator.models import Episode


class EntryTest(TestCase):
    def setUp(self):
        Episode(title='Sample', description='something', pub_date=timezone.now(),
                link='somelink', image='somelink', podcast_name='bla', guid='dskhfn').save()

    def test_entries_get(self):

        start = time.time()
        response = self.client.get(reverse('api-episodes'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.03)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
