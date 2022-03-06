from crum import get_current_user
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from phone_field import PhoneField


class Spending(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50, verbose_name='Tipo', choices=(
        ('cigarro', 'cigarro'),
        ('comida', 'comida'),
        ('bebida', 'bebida'),
        ('cafe', 'cafe'),
        ('aseo', 'aseo'),
        ('otro', 'otro'),
    ))
    cost = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Costo CUP', blank=True, null=True,
                               default=0.0,
                               validators=[MinValueValidator(0, message='Escriba un numero positivo'), ])
    cost_usd = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Costo USD', blank=True, null=True,
                                   default=0.0,
                                   validators=[MinValueValidator(0, message='Escriba un numero positivo'), ])
    date_creation = models.DateField(auto_now_add=True, verbose_name='Fecha', blank=True, null=True)
    quantify = models.PositiveSmallIntegerField(default=1, verbose_name='Cantidad', null=True, blank=True)
    description = models.CharField(max_length=222, verbose_name='Descripción', blank=True, null=True)

    def __str__(self):
        return self.type + f' {self.description}' if self.description else ''

    class Meta:
        verbose_name = 'Gasto'
        ordering = ['date_creation', 'type', 'description']

    def save(self, raw=False, force_insert=False,
             force_update=False, using=None, update_fields=None):
        user = get_current_user()
        self.user = user
        super(Spending, self).save()


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
            return format_html(f'<img src="{self.img.url}" class="circular agrandar" width="45" height="45" />')
        return 'No image'

    img_tag.short_description = 'Vista previa'

    def wash_tag(self):
        return mark_safe(
            f'<button name="_wash" type=button id="ropa{self.id}" class="btn circular btn-success">lavar</button>')

    wash_tag.short_description = 'Opciones'

    def save(self, raw=False, force_insert=False,
             force_update=False, using=None, update_fields=None):
        user = get_current_user()
        self.user = user
        super(Clothing, self).save()

    class Meta:
        verbose_name = 'Ropa'
        ordering = ['category', '-cont', 'name']
