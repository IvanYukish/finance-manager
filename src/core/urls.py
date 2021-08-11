from django.conf import settings
from django.urls import path

from core.views import HomeView, DebtsListView, DebtsCreateView, DebtsUpdateView, DebtsSynchronizeView, DebtsDetailView, \
    DebtsDeleteView, CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView, TransactionListView, \
    TransactionCreateView, TransactionUpdateView, TransactionDeleteView, TestPage

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('debts', DebtsListView.as_view(), name='debt-list'),
    path('debts/create', DebtsCreateView.as_view(), name='debt-create'),
    path('debts/synchronize', DebtsSynchronizeView.as_view(), name='debt-synchronize'),
    path('debts/<int:id>', DebtsDetailView.as_view(), name='debt-detail'),
    path('debts/<int:id>/update', DebtsUpdateView.as_view(), name='debt-update'),
    path('debts/<int:id>/delete', DebtsDeleteView.as_view(), name='debt-delete'),

    path('category', CategoryListView.as_view(), name='category-list'),
    path('category/create', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:id>/update', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:id>/delete', CategoryDeleteView.as_view(), name='category-delete'),

    path('transaction', TransactionListView.as_view(), name='transaction-list'),
    path('transaction/create', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:id>/update', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transaction/<int:id>/delete', TransactionDeleteView.as_view(), name='transaction-delete'),
]

# TODO remove it when app will in production
if settings.DEBUG:
    urlpatterns += [path('<str:page_name>', TestPage.as_view(), name='test-page')]
