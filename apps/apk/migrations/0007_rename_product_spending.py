# Generated by Django 4.0.2 on 2022-03-01 20:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apk', '0006_alter_product_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Spending',
        ),
    ]
