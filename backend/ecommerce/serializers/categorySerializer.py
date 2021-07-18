from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        field = ('id', 'name', 'created_at', 'updated_at')
