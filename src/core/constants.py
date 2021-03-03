from django.utils.translation import ugettext_lazy as _


class DebtMode:
    BORROW = '+'
    LEND = '-'

    MODE_CHOICES = (
        (BORROW, _('Позичити (у когось)')),
        (LEND, _('Позичити (комусь)')),
    )


class CategoryType:
    INCOME = '+'
    COST = '-'

    TYPE_CHOICES = (
        (INCOME, _('Дохід')),
        (COST, _('Витрата')),
    )
