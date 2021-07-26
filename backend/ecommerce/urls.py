from django.urls import include, path
from rest_framework import routers
from .views import ProductCatViewSet, ProductViewSet

router = routers.DefaultRouter()

# r'string' escape \ charachters, for example print(r'hello\nworld') prints same string where \n supposted be a new line
router.register(r'products', ProductViewSet)
router.register(r'categories', ProductCatViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
