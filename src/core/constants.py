from django.utils.translation import ugettext_lazy as _


class DebtMod:
    BORROW = '+'
    LEND = '-'

    MOD_CHOICES = (
        (BORROW, _('Позичати (у когось)')),
        (LEND, _('Позичити (комусь)')),
    )
