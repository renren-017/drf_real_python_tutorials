from django.test import TestCase
from rest_framework import status
from django.urls import reverse
import time

from flashcards.models import Card


def get_card():
    return Card.objects.last()


class CardTest(TestCase):
    def setUp(self):
        Card(question='SampleQ0', answer='SampleA0', box=2).save()

    def test_cards_get(self):

        start = time.time()
        response = self.client.get(reverse('api-cards'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cards_get_by_pk(self):

        start = time.time()
        response = self.client.get(reverse('api-card-detail', kwargs={'pk': get_card().pk}), format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cards_post(self):
        data = {
            'question': 'SampleQ',
            'answer': 'SampleA',
            'box': 1
        }

        start = time.time()
        response = self.client.post(reverse('api-cards'), data, format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_card_update(self):
        data = {
            'question': 'SampleQ Upd',
            'answer': 'SampleA Upd',
            'box': 5
        }
        start = time.time()
        response = self.client.put(reverse('api-card-detail', kwargs={'pk': get_card().pk}),
                                   data, format='json', content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_card_patch(self):
        data = {
            'box': 4
        }
        start = time.time()
        card = get_card()
        response = self.client.patch(reverse('api-card-detail', kwargs={'pk': card.pk}),
                                   data, format='json', content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(card.box, get_card().box)

    def test_card_delete(self):

        start = time.time()
        response = self.client.delete(reverse('api-card-detail', kwargs={'pk': get_card().pk}),
                                      format='json', content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
