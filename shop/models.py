from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    address = models.CharField(max_length=300)
    data = models.DateTimeField(auto_now_add = True)