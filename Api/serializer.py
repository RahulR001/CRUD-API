from rest_framework import serializers
from .models import APITodolist


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = APITodolist
        fields = '__all__'
