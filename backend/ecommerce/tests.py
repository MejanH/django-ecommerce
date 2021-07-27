from django.test import TestCase
from .models import Category, Product

# Create your tests here.


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_name(self):
        """
        Test the created Category name
        """
        self.assertEqual(self.category.name, 'Test Category')


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product', price=10.00, category=self.category)

    def test_product_name(self):
        """
        Test the created Product name
        """
        self.assertEqual(self.product.name, 'Test Product')

    def test_product_price(self):
        """
        Test the created Product price
        """
        self.assertEqual(self.product.price, 10.00)

    def test_product_category(self):
        """
        Test the created Product category
        """
        self.assertEqual(self.product.category, self.category)
