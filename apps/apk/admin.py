from django.contrib import admin
from django.conf.locale.es import formats
from .forms import *
from .models import *
from django.utils.html import format_html

formats.DATE_FORMAT = "d/M/Y"


# Inlines
class ClothingInline(admin.StackedInline):
    model = Clothing
    extra = 1
    form = ClothingForm


# ModelAdmins
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ClothingInline]


class SpendingAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'cost', 'cost_usd', 'quantify', 'date_creation',)
    form = ProductForm
    list_filter = ('type',)
    search_fields = ('description',)


class ClothingAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'category', 'name', 'cont', 'wash_tag')
    list_filter = ('category',)
    readonly_fields = ('img_tag',)
    form = ClothingForm
    search_fields = ('name',)
    actions = ['wash_selected', 'inc_cont', ]

    # exclude = ('img_tag', 'user')

    def get_queryset(self, request):
        qs = super(ClothingAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)

    def wash_selected(self, request, queryset):
        for q in queryset:
            q.cont = 0
            q.save()

    wash_selected.short_description = 'Lavar'

    def inc_cont(self, request, queryset):
        for q in queryset:
            q.cont += 1
            q.save()

    inc_cont.short_description = 'Aumentar puesta'


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Spending, SpendingAdmin)
admin.site.register(Clothing, ClothingAdmin)
