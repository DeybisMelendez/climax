from django.db import models
from customers.models import Customer
from datetime import date
from markdown import markdown
import math


class Quote(models.Model):
    number = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    contact = models.CharField(max_length=255, blank=True, default="El mismo")
    note = models.TextField(blank=True)
    date = models.DateField(default=date.today)
    currency = models.TextField(max_length=16, blank=True, default="Dólares")
    unit = models.CharField(max_length=4, blank=True, default="$")
    expiration = models.IntegerField(default=15, blank=True)

    def __str__(self):
        return f"No {self.number} de {self.customer.name}"

    def total(self):
        items = self.item_set.all()
        total = sum([item.total() for item in items])
        return total

    def get_description_md(self):
        return markdown(self.description)

    def get_note_md(self):
        return markdown(self.note)


class Item(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    quantity = models.DecimalField(
        decimal_places=2, max_digits=10, blank=False, null=False, default=1)
    description = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(
        decimal_places=2, max_digits=10, blank=False, null=False, default=1)

    def total(self):
        return self.quantity * self.price
