import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.utils import path_and_rename
from user.validators import phone_validator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email.lower())
        user = self.model(
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.username = email
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(_('Аватар'), upload_to=path_and_rename, blank=True, null=True, default=None)
    phone_number = models.CharField(_('Номер Телефону'), max_length=20, validators=[phone_validator], null=True,
                                    blank=True)
    email = models.EmailField(_('Поштова адреса'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Користувач')
        verbose_name_plural = _('Користувачі')

    def __str__(self):
        return f'{self.get_full_name() or self.email}'
