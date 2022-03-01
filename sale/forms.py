from django import forms

from sale.models import Product, ProdCategory


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['s_price'].widget.attrs['class'] = 'form-control'
        self.fields['p_price'].widget.attrs['class'] = 'form-control'
        self.fields['cat'].widget.attrs['class'] = 'form-control'
        self.fields['stock'].widget.attrs['class'] = 'form-control'
        self.fields['is_active'].widget.attrs['class'] = 'form-control'
        self.fields['priority'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'desc': forms.Textarea(
                attrs={
                    'placeholder': 'Una breve descripción opcional',
                    'rows': 3,
                    'cols': '3',
                    'class': 'form-control',
                }
            ),
        }


class ProdCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = ProdCategory
        fields = '__all__'
        widgets = {
            'desc': forms.Textarea(
                attrs={
                    'placeholder': 'Una breve descripción opcional',
                    'rows': 3,
                    'cols': '3',
                    'class': 'form-control',
                }
            ),
        }
