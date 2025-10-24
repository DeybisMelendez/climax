from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ruc = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
