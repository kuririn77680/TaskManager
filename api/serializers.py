# api/serializers.py

from rest_framework import serializers
from app import models


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = '__all__'
