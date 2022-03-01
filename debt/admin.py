from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import *
from .forms import *


# class ClientInline(admin.StackedInline):
#     extra = 0
#     model = Client


class DebtInline(admin.StackedInline):
    extra = 3
    model = Debt


class DebtAdmin(admin.ModelAdmin):
    list_display = ('client', 'description', 'quantify', 'date_creation', 'date_to_pay')
    form = DebtForm

    # list_filter = (('date_creation', DateRangeFilter),)

    def get_queryset(self, request):
        qs = super(DebtAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(client__user=request.user)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'get_debts')
    form = ClientForm
    inlines = [DebtInline]
    actions = ['delete_debts']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def delete_debts(self, request, queryset):
        for qs in queryset:
            for debt in Debt.objects.filter(client=qs):
                debt.delete()

    delete_debts.short_description = 'Eliminar deudas'


admin.site.register(Client, ClientAdmin)
admin.site.register(Debt, DebtAdmin)
