# Generated by Django 4.0.2 on 2022-03-01 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0005_alter_product_options_alter_product_cost_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['date_creation', 'type', 'description'], 'verbose_name': 'Gasto'},
        ),
    ]
