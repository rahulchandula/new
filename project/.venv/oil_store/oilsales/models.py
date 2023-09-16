from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products_ordered = models.ManyToManyField(Product, through='OrderItem')
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
