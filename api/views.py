# Create your views here.
from app import models
from api import serializers
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
