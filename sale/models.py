from crum import get_current_user
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import format_html

priority_choices = (
    ('High', 'Alta'),
    ('Normal', 'Normal'),
    ('Low', 'Baja'),
)


class ProdCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Productos'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cat = models.ForeignKey(ProdCategory, on_delete=models.CASCADE, verbose_name='Categoría')
    name = models.CharField(verbose_name='Nombre', max_length=100, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    stock = models.PositiveIntegerField(default=1, verbose_name='Cantidad', )
    p_price = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Costo CUP',
                                  validators=[MinValueValidator(0, message='Escriba un numero positivo'), ])
    s_price = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Precio CUP',
                                  validators=[MinValueValidator(0, message='Escriba un numero positivo'), ])
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')
    priority = models.CharField(max_length=22, choices=priority_choices, default='Low', verbose_name='Prioridad')
    is_active = models.BooleanField(default=True, verbose_name='Esta disponible')

    def __str__(self):
        return self.name

    def save(self, raw=False, force_insert=False,
             force_update=False, using=None, update_fields=None):
        user = get_current_user()
        self.user = user
        super(Product, self).save()

    def img_tag(self):
        url = '/static/img/empty.png'
        if self.image:
            url = self.image.url
        return format_html(f'<img src="{url}" class="circular agrandar" width="45" height="45" />')

    img_tag.short_description = 'Imagen'

    class Meta:
        ordering = ['cat', '-is_active', 'name', 'stock']
        verbose_name = 'Producto'
