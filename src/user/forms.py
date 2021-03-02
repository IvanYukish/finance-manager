from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(label=_('Ім\'я'), max_length=150,
                                 widget=forms.TextInput(attrs={'placeholder': _('Введіть своє ім\'я')}))
    last_name = forms.CharField(label=_('Прізвище'), max_length=150,
                                widget=forms.TextInput(attrs={'placeholder': _('Введіть своє прізвище')}))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'avatar']
