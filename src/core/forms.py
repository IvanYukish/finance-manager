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
        widgets = {
            'debtor_name': forms.TextInput(
                attrs={'class': 'form-control form-input-height', 'placeholder': 'Debtor name', 'required': 'True'}),
            'mode': forms.Select(attrs={'class': 'form-control form-input-height', 'placeholder': 'Type'}),
            'prise': forms.NumberInput(attrs={'class': 'form-control form-input-height', 'placeholder': 'Prise'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control form-input-height', 'placeholder': 'Description'}),
        }

        # username = forms.CharField(label="User Name:*", widget=forms.TextInput(attrs={'class': 'form-control'}))
        # email = forms.EmailField(required=False, label="Email:",
        #                          widget=forms.EmailInput(attrs={'class': 'form-control', 'requered': 'false'}))
        # first_name = forms.CharField(required=False, label="First Name:",
        #                              widget=forms.TextInput(attrs={'class': 'form-control'}))
        # last_name = forms.CharField(required=False, label="Last Name:",
        #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
        # password1 = forms.CharField(label="Password:*", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        # password2 = forms.CharField(label="Confirm password:*",
        #                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CategoryForm(UserHiddenInput):
    class Meta:
        model = Category
        fields = ['user', 'name', 'type', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-input-height', 'placeholder': 'Category name', 'required': 'True'}),
            'type': forms.Select(attrs={'class': 'form-control form-input-height', 'placeholder': 'Type'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control form-input-height', 'placeholder': 'Description'}),
        }


class TransactionForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].empty_label="Category not selected"
    class Meta:
        model = Transaction
        fields = ['prise', 'category', 'description']
        widgets = {
            'prise': forms.NumberInput(attrs={'class': 'form-control form-input-height', 'placeholder': 'Prise'}),
            'category': forms.Select(attrs={'class': 'form-control form-input-height'}, ),
            'description': forms.Textarea(
                attrs={'class': 'form-control form-input-height', 'placeholder': 'Description'}),
        }
