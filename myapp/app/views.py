from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework import generics


class TasksList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Task.objects.all()


class TaskCreate(generics.CreateAPIView):
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Task.objects.all()
