from django.urls import path

from .views import (
    ToDoListView, ToDoListDetailView, ToDoListCreateView,
    ToDoListUpdateView, ToDoListDeleteView,

    TaskListView, TaskCreateView, 
    TaskUpdateView, TaskDeleteView,
)


urlpatterns = [
    # To-Do List URLs
    path('lists/', ToDoListView.as_view(), name='todolist-list'),
    path('lists/<int:pk>/', ToDoListDetailView.as_view(), name='todolist-detail'),
    path('lists/add/', ToDoListCreateView.as_view(), name='todolist-create'),
    path('lists/<int:pk>/edit/', ToDoListUpdateView.as_view(), name='todolist-update'),
    path('lists/<int:pk>/delete/', ToDoListDeleteView.as_view(), name='todolist-delete'),

    # Task URLs
    path('lists/<int:pk>/tasks/', TaskListView.as_view(), name='task-list'),
    path('lists/<int:pk>/tasks/add/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
