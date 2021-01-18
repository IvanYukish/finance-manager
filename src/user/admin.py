from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
