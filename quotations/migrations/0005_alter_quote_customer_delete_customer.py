# Generated by Django 4.1.7 on 2023-04-02 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('quotations', '0004_alter_quote_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
