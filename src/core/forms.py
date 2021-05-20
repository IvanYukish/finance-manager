from crispy_forms.layout import Layout, Field
from django import forms

from core.constants import CategoryType
from core.models import Debt, Category, Transaction
from crispy_forms.helper import FormHelper


class UserHiddenInput(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()


class DebtForm(UserHiddenInput):
    class Meta:
        model = Debt
        fields = ['user', 'debtor_name', 'mode', 'prise', 'description']
        widgets = {
            'debtor_name': forms.TextInput(
                attrs={'placeholder': 'Ім\'я',
                       'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-1'}),
            'mode': forms.Select(attrs={
                'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-2'},
            ),
            'description': forms.Textarea(attrs={'placeholder': 'Опис',
                                                 'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-3'},
                                          ),
            'prise': forms.NumberInput(
                attrs={'min': '0',
                       'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-1'}),

        }


class CategoryForm(UserHiddenInput):
    class Meta:
        model = Category
        fields = ['user', 'name', 'description', 'type']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Ім\'я',
                       'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-1'}),
            'type': forms.Select(attrs={
                'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-2'},
            ),
            'description': forms.Textarea(attrs={'placeholder': 'Опис',
                                                 'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-3'},
                                          ),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['prise', 'description', 'category']
        widgets = {
            'prise': forms.NumberInput(
                attrs={'min': '0',
                       'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-1'}),
            'category': forms.Select(attrs={
                'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-2'},
            ),
            'description': forms.Textarea(attrs={'placeholder': 'Опис',
                                                 'class': 'u-border-1 u-border-palette-5-dark-1 u-input u-input-rectangle u-radius-5  u-input-3'},
                                          )
        }
