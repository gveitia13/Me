from django import forms

from apps.apk.models import *


class ClothingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClothingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Clothing
        fields = '__all__'
        exclude = ('user', 'img_tag',)


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Clothing
        fields = '__all__'
        exclude = ('user',)
