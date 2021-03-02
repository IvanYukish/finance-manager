from django.db.models.signals import post_save
from django.dispatch import receiver

from user.constants import CATEGORY_FIXTURE
from user.models import CustomUser
from core.models import Category


@receiver(post_save, sender=CustomUser)
def create_fixture_category(sender, instance, created, **kwargs):
    if created:
        Category.objects.bulk_create(
            [Category(user=instance, name=i[0], type=i[1]) for i in CATEGORY_FIXTURE])
    else:
        pass


post_save.connect(create_fixture_category, sender=CustomUser)