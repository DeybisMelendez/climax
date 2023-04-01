# Generated by Django 4.1.7 on 2023-04-01 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0002_delete_item_quote_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='items',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotations.quote')),
            ],
        ),
    ]
