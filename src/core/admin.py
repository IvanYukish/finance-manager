from django.contrib import admin

from core.models import Debt, Category


class DebtsAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Debt, DebtsAdmin)
admin.site.register(Category, CategoryAdmin)
