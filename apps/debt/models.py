from crum import get_current_user
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from phone_field import PhoneField


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    phone = models.CharField(blank=True, max_length=30, help_text='Número del celular', verbose_name='Celular')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, raw=False, force_insert=False,
             force_update=False, using=None, update_fields=None):
        user = get_current_user()
        self.user = user
        super(Client, self).save()

    def __str__(self):
        return self.name

    def get_debts(self):
        debts = ''
        for d in Debt.objects.filter(client=self):
            debts += f'<a href="/admin/debt/debt/{d.id}/change/">' \
                     f' <span class="badge badge-success circular">' \
                     f'{d.description}: {d.quantify}</span></a> '
        if debts == '': return mark_safe('<b>No tiene deudas</b>')
        return mark_safe(debts)

    get_debts.short_description = 'Deudas'

    class Meta:
        verbose_name = 'Cliente'
        ordering = ['name']


class Debt(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente', null=True, blank=True)
    description = models.CharField(max_length=222, verbose_name='Descripción')
    quantify = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Cantidad',
                                   validators=[MinValueValidator(0, message='Escriba un numero positivo'), ])
    date_creation = models.DateField(auto_now_add=True, verbose_name='Fecha', blank=True, null=True)
    date_to_pay = models.DateField(verbose_name='Dia a pagar', null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Deuda'
        ordering = ['client', 'date_creation', 'quantify']
