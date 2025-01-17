from django.db import models
from customers.models import Customer

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    sentiment = models.CharField(max_length=20)  

    def __str__(self):
        return f"{self.customer.username} - {self.product.name}"