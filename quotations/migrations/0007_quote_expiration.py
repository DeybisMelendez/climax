# Generated by Django 4.1.7 on 2023-04-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0006_quote_contact_quote_currency_quote_date_quote_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='expiration',
            field=models.IntegerField(blank=True, default=15),
        ),
    ]