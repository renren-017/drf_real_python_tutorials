from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
import time

from projects.models import Project


def temporary_image():
    bio = BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bio, 'jpeg')
    return SimpleUploadedFile("test.jpg", bio.getvalue())


class ProjectTest(TestCase):

    def setUp(self):
        Project(title='Sample', description='Sample description', technology='Python/Django',
                image=temporary_image()).save()

    def test_get_projects(self):
        start = time.time()
        response = self.client.get(reverse('api-projects'), format='json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_by_pk(self):
        project_id = Project.objects.last().pk

        start = time.time()
        response = self.client.get(reverse('api-project-detail', kwargs={'pk': project_id}), format='json')
        end = time.time()

        self.assertLess(end - start, 0.01)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

