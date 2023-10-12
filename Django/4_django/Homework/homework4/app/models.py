from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    date_registered = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


