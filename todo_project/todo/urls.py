from django.urls import path
from .views import TodoCreateView, TodoListView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('list/', TodoListView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
]
