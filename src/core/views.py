from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.base import View

from core.forms import DebtForm, CategoryForm, TransactionForm
from core.models import Debt, Category, Transaction


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html', {})


class DebtsListView(LoginRequiredMixin, ListView):
    model = Debt
    template_name = 'core/debt_list.html'
    context_object_name = 'debts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class DebtsDetailView(DetailView):
    model = Debt
    template_name = 'core/debt_detail.html'
    context_object_name = 'debt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_object(self, queryset=None):
        debt_id = int(self.kwargs.get('id'))
        return Debt.objects.get(id=debt_id)


class DebtsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Debt
    template_name = 'core/debt_create.html'
    context_object_name = 'debts'
    success_url = reverse_lazy('core:debt-list')
    success_message = _('Ваш боржник був успішно створений')
    form_class = DebtForm

    def get_initial(self):
        return {'user': self.request.user}


class DebtsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Debt
    template_name = 'core/debt_list.html'
    context_object_name = 'debt'
    success_url = reverse_lazy('core:debt-list')
    success_message = _('Ваш боржник був успішно Видалений')

    def get_object(self, queryset=None):
        debt_id = int(self.kwargs.get('id'))
        return self.model.objects.get(id=debt_id)

    def test_func(self):
        return self.request.user == self.get_object().user


class DebtsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = Debt
    form_class = DebtForm
    template_name = 'core/debt_update.html'
    context_object_name = 'debt'
    success_message = _('Дані про боржника були успішно змінені')

    def get_object(self, queryset=None):
        debt_id = int(self.kwargs.get('id'))
        return self.model.objects.get(id=debt_id)

    def get_success_url(self):
        return reverse_lazy('core:debt-detail', args=(self.kwargs.get('id'),))

    def test_func(self):
        return self.request.user == self.get_object().user


class DebtsSynchronizeView(View):
    pass


class CategoryCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'core/category_create.html'
    context_object_name = 'category'
    success_message = _('Категорія була успішно додана')

    def get_initial(self):
        return {'user': self.request.user}


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.filter(Q(user=self.request.user) | Q(user=None))


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'core/category_update.html'
    context_object_name = 'category'
    success_message = _('Дані про категорію були успішно змінені')

    def get_object(self, queryset=None):
        category_id = int(self.kwargs.get('id'))
        return self.model.objects.get(id=category_id)

    def test_func(self):
        return self.request.user == self.get_object().user


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, SuccessMessageMixin):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'categories'
    success_url = reverse_lazy('core:category-list')
    success_message = _('Категорія успішно видалена!')

    def get_object(self, queryset=None):
        category_id = int(self.kwargs.get('id'))
        return self.model.objects.get(id=category_id)

    def test_func(self):
        return self.request.user == self.get_object().user


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'core/transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return self.model.objects.filter(category__user=self.request.user)


class TransactionCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/transaction_create.html'
    context_object_name = 'transaction'
    success_message = _('Транзакція була успішно додана')

    def get_form_kwargs(self):
        kwargs = super(TransactionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TransactionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/transaction_update.html'
    context_object_name = 'transaction'
    success_message = _('Дані про транзакцію були успішно змінені')

    def get_form_kwargs(self):
        kwargs = super(TransactionUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        transaction_id = int(self.kwargs.get('id'))
        return self.model.objects.get(id=transaction_id)

    def test_func(self):
        return self.request.user == self.get_object().category.user


class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, SuccessMessageMixin):
    model = Transaction
    template_name = 'core/transaction_list.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('core:transaction-list')
    success_message = _('Транзакція успішно видалена!')

    def get_object(self, queryset=None):
        transaction_id = int(self.kwargs.get('id'))
        return self.model.objects.get(id=transaction_id)

    def test_func(self):
        return self.request.user == self.get_object().category.user


# TODO remove it when app will ready to production
class TestPage(TemplateView):

    @property
    def template_name(self):
        template_path = f'test_pages/{self.request.path}'

        try:
            get_template(template_path)
        except TemplateDoesNotExist:
            raise Http404('Template with this name does not exists')

        return template_path
