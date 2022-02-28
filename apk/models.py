import os

from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from Ropa.settings import BASE_DIR


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50, verbose_name='Tipo', choices=(
        ('cigarro', 'cigarro'),
        ('comida', 'comida'),
        ('bebida', 'bebida'),
        ('cafe', 'cafe'),
        ('aseo', 'aseo'),
        ('otro', 'otro'),
    ))
    date_creation = models.DateField(auto_now_add=True, verbose_name='Fecha de comprado', blank=True, null=True)
    description = models.CharField(max_length=222, verbose_name='Decripcion', blank=True, null=True)

    def __str__(self):
        return self.type + f' {self.description}' if self.description else ''

    class Meta:
        verbose_name = 'Producto'
        ordering = ['date_creation']

    def save(self, raw=False, force_insert=False,
             force_update=False, using=None, update_fields=None):
        user = get_current_user()
        self.user = user
        super(Product, self).save()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'


class Clothing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='ropa/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    cont = models.PositiveSmallIntegerField(verbose_name='Veces puestas', default=0)
    name = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.name

    def img_tag(self):
        if self.img:
            return format_html(f'<img src="{self.img.url}" width="60" height="60" />')
        return 'No image'

    img_tag.short_description = 'Imagen'

    def save(self, raw=False, force_insert=False,
             force_update=False, using=None, update_fields=None):
        user = get_current_user()
        self.user = user
        super(Clothing, self).save()

    class Meta:
        verbose_name = 'Ropa'
        ordering = ['category', '-cont', 'name']
