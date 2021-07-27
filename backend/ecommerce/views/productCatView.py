from rest_framework import permissions, viewsets
from ..serializers import CategorySerializer
from ..models import Category


class ProductCatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
