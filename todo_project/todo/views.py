from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

# Create: POST
class TodoCreateView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Read: GET List
class TodoListView(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Read: GET Single Item
class TodoDetailView(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Update: PUT
class TodoUpdateView(generics.UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Delete: DELETE
class TodoDeleteView(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
