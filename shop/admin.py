from django.contrib import admin
from .models import Product
from .models import Order


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('title',)


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product',)

