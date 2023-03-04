from .models import *
from rest_framework import serializers


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'text', 'status', 'deadline']
