from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
import base64


class TodoItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client = APIClient()

    def test_create_read_integration(self):
        # Authenticate the client with the correct username and password
        auth_header = f'Basic {base64.b64encode(f"testuser:testpassword".encode()).decode()}'
        self.client.credentials(HTTP_AUTHORIZATION=auth_header)

        # Create a new todo item
        data = {'title': 'New Task',
                'description': 'New Description', 'status': 'OPEN'}
        response_create = self.client.post('/api/todo/create/', data)
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)

        # Attempt to read the created todo item
        todo_id = response_create.data.get("id")
        response_read = self.client.get(f'/api/todo/{todo_id}/')
        self.assertEqual(response_read.status_code, status.HTTP_200_OK)
