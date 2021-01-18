from django.contrib import admin

from core.models import Debt, Category, Income


class DebtsAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class IncomeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Debt, DebtsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Income, IncomeAdmin)
