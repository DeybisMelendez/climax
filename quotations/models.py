from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ruc = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    number = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    note = models.TextField()

    def __str__(self):
        return f"No {self.number} - Cliente: {self.customer.name}"

    def total(self):
        items = self.item_set.all()
        total = sum([item.total() for item in items])
        return total


class Item(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(
        decimal_places=2, max_digits=10, blank=False, null=False)

    def total(self):
        return self.quantity * self.price
