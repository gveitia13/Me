from django.contrib import admin

from sale.forms import *
from sale.models import *


class ProdCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    form = ProdCategoryForm

    def get_queryset(self, request):
        qs = super(ProdCategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(product__user=request.user)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'cat', 'name', 'p_price', 's_price', 'stock', 'is_active')
    form = ProductForm
    actions = ['deactivate', 'activate']
    list_filter = ('is_active',)
    fieldsets = [
        ('Principal', {
            'fields': ('cat', 'name', 'p_price', 's_price')
        },),
        ('Extra', {
            'fields': ('image', 'stock', 'priority', 'is_active', 'desc')
        })
    ]

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def deactivate(self, request, queryset):
        for p in queryset:
            p.is_active = False
            p.save()

    deactivate.short_description = 'Desactivar'

    def activate(self, request, queryset):
        for p in queryset:
            p.is_active = True
            p.save()

    activate.short_description = 'Activar'


admin.site.register(ProdCategory, ProdCategoryAdmin)
admin.site.register(Product, ProductAdmin)
