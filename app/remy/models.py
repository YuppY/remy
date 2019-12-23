from django.core import validators
from django.db import models


class MenuItem(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_items = models.ManyToManyField(MenuItem, through='OrderItem')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    count = models.IntegerField(validators=[validators.MinValueValidator(1)])
