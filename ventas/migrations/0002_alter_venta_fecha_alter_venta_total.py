# Generated by Django 4.2.16 on 2024-11-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=100, null=True),
        ),
    ]