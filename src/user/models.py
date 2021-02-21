import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.utils import path_and_rename
from user.validators import phone_validator


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(_('Аватар'), upload_to=path_and_rename, blank=True, null=True, default=None)
    phone_number = models.CharField(_('Номер Телефону'), max_length=20, validators=[phone_validator], null=True,
                                    blank=True)
    email = models.EmailField(_('Поштова адреса'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Користувач')
        verbose_name_plural = _('Користувачі')

    def __str__(self):
        return f'{self.get_full_name() or self.email}'
