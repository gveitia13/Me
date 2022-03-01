from django import forms

from debt.models import Debt, Client


class DebtForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DebtForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Debt
        fields = '__all__'


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('user',)
