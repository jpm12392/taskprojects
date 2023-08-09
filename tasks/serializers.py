from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class LoginSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']