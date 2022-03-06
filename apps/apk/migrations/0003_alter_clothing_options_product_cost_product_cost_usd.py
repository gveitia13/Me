# Generated by Django 4.0.2 on 2022-02-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apk', '0002_alter_category_options_alter_clothing_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothing',
            options={'ordering': ['category', '-cont', 'name'], 'verbose_name': 'Ropa'},
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Costo'),
        ),
        migrations.AddField(
            model_name='product',
            name='cost_usd',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='Costo USD'),
        ),
    ]