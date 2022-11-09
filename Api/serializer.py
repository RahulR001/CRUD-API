from rest_framework import serializers
from .models import APITodolist


# ========== class-to-create-serializer ==========

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = APITodolist
        fields = ['tasktitle','taskDesc']
