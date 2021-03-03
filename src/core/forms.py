from django import forms
from core.models import Debt, Category, Transaction


class UserHiddenInput(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()


class DebtForm(UserHiddenInput):
    class Meta:
        model = Debt
        fields = ['user', 'debtor_name', 'mode', 'prise', 'description']


class CategoryForm(UserHiddenInput):
    class Meta:
        model = Category
        fields = ['user', 'name', 'description', 'type']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['prise', 'description', 'category']
