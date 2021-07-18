from django.contrib import admin
from .models import Product, Category

admin.site.site_header = 'E-commerce Admin'
admin.site.site_title = 'E-commerce Admin'

# Register your models here.
admin.site.register([Product, Category])
