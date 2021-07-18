from rest_framework import viewsets
from ..serializers import CategorySerializer
from ..models import Category


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
