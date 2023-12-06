from django.urls import path
from .views import TodoItemCreateView
from .views import TodoItemUpdateView
from .views import TodoItemDeleteView
from .views import TodoItemListReadView
from .views import TodoItemReadView
urlpatterns = [
    path('create/', TodoItemCreateView.as_view(), name='todo-create'),
    path('<int:pk>/', TodoItemReadView.as_view(), name='todo-read'),
    path('list/', TodoItemListReadView.as_view(),
         name='todo-list'),
    path('update/<int:pk>/', TodoItemUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoItemDeleteView.as_view(), name='todo-delete'),
]
