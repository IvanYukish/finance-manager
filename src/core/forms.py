from django import forms
from core.models import Debt


class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['user', 'debtor_name', 'mod', 'prise', 'description']
