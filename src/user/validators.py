from django.core import validators
from django.utils.translation import ugettext_lazy as _


class CustomPhoneNumberValidator(validators.RegexValidator):
    regex = r'^\+380[0-9]{9}$'
    message = _("Формат:'+380123456789'")


phone_validator = CustomPhoneNumberValidator()
