from django import forms
from core.models import Debts


class DebtForm(forms.ModelForm):
    class Meta:
        model = Debts
        fields = ['user', 'debtor_name', 'mod', 'prise', 'description']
