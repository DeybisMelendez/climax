from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Entry(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Entry of {self.quantity} units of {self.product.name} on {self.created_at}'


class Exit(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Exit of {self.quantity} units of {self.product.name} on {self.created_at}'
