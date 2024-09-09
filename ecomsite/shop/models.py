from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    # image = models.CharField(max_length=300)


    def __str__(self) -> str:
        return self.title

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)
    total = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name





