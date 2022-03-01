# Generated by Django 4.0.2 on 2022-03-01 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0004_product_quantify_alter_product_cost_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['date_creation', 'type', 'description'], 'verbose_name': 'Producto'},
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0, message='Escriba un numero positivo')], verbose_name='Costo CUP'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost_usd',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0, message='Escriba un numero positivo')], verbose_name='Costo USD'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_creation',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha'),
        ),
    ]