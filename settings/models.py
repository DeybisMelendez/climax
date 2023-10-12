from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32)
    symbol = models.CharField(max_length=3)

    def __str__(self):
        return self.name
