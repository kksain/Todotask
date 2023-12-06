from django.test import TestCase
from todo.models import TodoItem, Tag


class TodoItemModelTest(TestCase):
    def test_todo_item_creation(self):
        todo_item = TodoItem.objects.create(
            title='Test Task', description='Test Description', status='OPEN')
        self.assertEqual(str(todo_item), 'Test Task')


class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')
