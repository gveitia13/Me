# Generated by Django 4.0.2 on 2022-03-01 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debt', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='debt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='debt.debt', verbose_name='Deuda'),
        ),
    ]
