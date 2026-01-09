from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        decimal_places=2, max_digits=8, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name


class UserItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(
        decimal_places=2, max_digits=8, blank=True, null=True
    )
    total = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
