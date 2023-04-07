# Generated by Django 4.1.7 on 2023-04-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0007_quote_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
