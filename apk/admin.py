from django.contrib import admin

from .forms import *
from .models import *
from django.utils.html import format_html

es_formats.DATE_FORMAT = "d/M/Y"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'cost', 'cost_usd', 'quantify', 'date_creation',)
    form = ProductForm


class ClothingAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'category', 'name', 'cont', 'wash_tag')
    readonly_fields = ('img_tag',)
    form = ClothingForm

    # exclude = ('img_tag', 'user')

    def get_queryset(self, request):
        qs = super(ClothingAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Clothing, ClothingAdmin)
