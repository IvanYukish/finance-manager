from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.constants import DebtMode, CategoryType
from user.models import CustomUser


class AbstractDateTimeModel(models.Model):
    created_at = models.DateTimeField(_('Створено'), default=timezone.now)
    modified_at = models.DateTimeField(_('Модифіовано'), null=True, blank=True)

    class Meta:
        abstract = True


class Debt(AbstractDateTimeModel):
    user = models.ForeignKey(get_user_model(), related_name='debt', on_delete=models.CASCADE)
    debtor_name = models.CharField(_('Ім\'я'), max_length=100)
    mode = models.CharField(_('Модифікатор'), choices=DebtMode.MODE_CHOICES, max_length=1, default='-')
    prise = models.PositiveIntegerField(_('Значення'))
    description = models.CharField(_('Опис'), max_length=500)
    debt_time = models.DateTimeField(_('Час зміни'), default=timezone.now)

    class Meta:
        verbose_name = _('Борг')
        verbose_name_plural = _('Борги')
        constraints = [
            models.UniqueConstraint(fields=['user', 'debtor_name'], name='debtor constraint')
        ]

    def __str__(self):
        return f'{self.debtor_name}- {self.prise}'


class Category(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='category', on_delete=models.CASCADE)
    name = models.CharField(_('Ім\'я'), max_length=40)
    description = models.TextField(_('Опис'), max_length=500, null=True, blank=True)
    type = models.CharField(_('Тип'), choices=CategoryType.TYPE_CHOICES, max_length=1, default=DebtMode.LEND)

    class Meta:
        verbose_name = _('Категорія')
        verbose_name_plural = _('Категорії')
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='category constraint')
        ]

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('core:category-list')


class Transaction(AbstractDateTimeModel):
    prise = models.PositiveIntegerField(_('Сума'), )
    description = models.TextField(_('Опис'), max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='transaction', on_delete=models.CASCADE)
    date = models.DateTimeField(_('Час виконання'), default=timezone.now)

    class Meta:
        verbose_name = _('Транзакція')
        verbose_name_plural = _('Транзакції')

    def __str__(self):
        return f'{self.prise} - {self.category}'

    def get_absolute_url(self):
        return reverse('core:transaction-list')
