# Generated by Django 4.1.7 on 2023-10-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('quotations', '0009_quote_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='unit',
        ),
        migrations.AddField(
            model_name='quote',
            name='currency_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.currency'),
        ),
    ]