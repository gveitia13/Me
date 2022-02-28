from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'date_creation',)


class ClothingAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'category', 'name', 'cont',)
    readonly_fields = ('img_tag',)

    def get_queryset(self, request):
        qs = super(ClothingAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Clothing, ClothingAdmin)
