from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from django.urls import reverse
import time

from to_do.models import ToDoList, ToDoItem


def get_todolist():
    return ToDoList.objects.all().last()


def get_todoitem():
    return ToDoItem.objects.all().last()


class ToDoListTest(TestCase):

    def setUp(self):
        ToDoList(title='Sample').save()

    def test_get_todolists(self):
        start = time.time()
        response = self.client.get(reverse('api-todolists'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_todolists(self):
        data = {
            'title': 'Sample 2'
        }
        start = time.time()
        response = self.client.post(reverse('api-todolists'), data, format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_todolists_by_pk(self):
        start = time.time()
        todolist_pk = get_todolist().pk
        response = self.client.get(reverse('api-todolist-detail', kwargs={'pk': todolist_pk}), format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todolists_by_pk(self):
        start = time.time()
        todolist_pk = get_todolist().pk
        response = self.client.delete(reverse('api-todolist-detail', kwargs={'pk': todolist_pk}), format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ToDoItemTest(TestCase):

    def setUp(self):
        ToDoList(title='Sample').save()
        ToDoItem(title='Sample To Do', description='Lorem Ipsum',
                 due_date=timezone.now(), todo_list=get_todolist()).save()

    def test_item_create(self):
        data = {
            'title': 'Sample To Do 2',
            'description': 'Lorem Ipsum 2',
        }
        start = time.time()
        response = self.client.post(reverse('api-todoitem-create', kwargs={'pk': get_todolist().pk}),
                                    data, format='json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_update(self):
        data = {
            'title': 'Sample To Do 2 Upd',
            'description': 'Lorem Ipsum 2 Upd',
        }
        start = time.time()
        response = self.client.put(reverse('api-todoitem-detail', kwargs={'pk': get_todoitem().pk}),
                                    data, format='json', content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_delete(self):
        start = time.time()
        response = self.client.delete(reverse('api-todoitem-detail', kwargs={'pk': get_todoitem().pk}),
                                   format='json', content_type='application/json')
        end = time.time()

        self.assertLess(end - start, 0.02)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
