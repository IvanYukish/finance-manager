from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.constants import DebtMod
from user.models import CustomUser


class AbstractDateTimeModel(models.Model):
    created_at = models.DateTimeField(_('Створено'), default=timezone.now)
    modified_at = models.DateTimeField(_('Модифіовано'), null=True, blank=True)

    class Meta:
        abstract = True


class Debts(AbstractDateTimeModel):
    user = models.ForeignKey(CustomUser, related_name='debt', on_delete=models.CASCADE)
    debtor_name = models.CharField(_('Ім\'я'), max_length=100)
    mod = models.CharField(_('Модифікатор'), choices=DebtMod.MOD_CHOICES, max_length=1)
    prise = models.PositiveIntegerField(_('Значення'))
    description = models.CharField(_('Опис'), max_length=500)
    debt_time = models.DateTimeField(_('Час зміни'), default=timezone.now)

    class Meta:
        verbose_name = _('Борг')
        verbose_name_plural = _('Борги')

    def __str__(self):
        return f'{self.debtor_name}- {self.prise}'


class Category(models.Model):
    name = models.CharField(_('Ім\'я'), max_length=40)
    description = models.TextField(_('Опис'), max_length=500)

    class Meta:
        verbose_name = _('Категорія')
        verbose_name_plural = _('Категорії')

    def __str__(self):
        return f'{self.name}'


class Income(AbstractDateTimeModel):
    user = models.ForeignKey(CustomUser, related_name='income', on_delete=models.CASCADE)
    prise = models.PositiveIntegerField(_('Прибуток'), )
    description = models.PositiveIntegerField(_('Опис'), )
    category = models.ForeignKey(Category, related_name='income', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Прибуток')
        verbose_name_plural = _('Прибутки')

    def __str__(self):
        return f'{self.prise} - {self.category}'


class Cost(AbstractDateTimeModel):
    user = models.ForeignKey(CustomUser, related_name='cost', on_delete=models.CASCADE)
    prise = models.PositiveIntegerField(_('Витрата'), )
    description = models.PositiveIntegerField(_('Опис'), )
    category = models.ForeignKey(Category, related_name='cost', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Витрата')
        verbose_name_plural = _('Витрати')

    def __str__(self):
        return f'{self.prise} - {self.category}'
