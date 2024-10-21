from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

# CRUD
class ListTodo(generics.ListCreateAPIView):    #read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView): # update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):  # create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DeleteTodo(generics.DestroyAPIView):   # delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

