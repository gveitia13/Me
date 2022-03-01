from daterangefilter.filters import DateRangeFilter
from django.contrib import admin
from .models import *
from .forms import *


class ClientInline(admin.StackedInline):
    extra = 1
    model = Client


class DebtAdmin(admin.ModelAdmin):
    list_display = ('get_client', 'description', 'quantify', 'date_creation', 'date_to_pay')
    form = DebtForm
    # list_filter = (('date_creation', DateRangeFilter),)
    inlines = [ClientInline, ]

    def get_queryset(self, request):
        qs = super(DebtAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(client__user=request.user)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'get_debts')
    form = ClientForm

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(Client, ClientAdmin)
admin.site.register(Debt, DebtAdmin)
