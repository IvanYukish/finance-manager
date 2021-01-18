from django.urls import path, include

from core.views import HomeView, DebtsListView, DebtsCreateView, DebtsUpdateView, DebtsSynchronizeView, DebtsDetailView, \
    DebtsDeleteView

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('debts', DebtsListView.as_view(), name='debt-list'),
    path('debts/create', DebtsCreateView.as_view(), name='debt-create'),
    path('debts/synchronize', DebtsSynchronizeView.as_view(), name='debt-synchronize'),
    path('debts/<int:id>', DebtsDetailView.as_view(), name='debt-detail'),
    path('debts/<int:id>/update', DebtsUpdateView.as_view(), name='debt-update'),
    path('debts/<int:id>/delete', DebtsDeleteView.as_view(), name='debt-delete'),
]
