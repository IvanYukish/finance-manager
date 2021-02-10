from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.base import View

from core.forms import DebtForm
from core.models import Debt


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
    success_url = reverse_lazy('core:home')
    success_message = _('Ваш боржник був успішно створений')
    form_class = DebtForm

    def get_context_data(self, **kwargs):
        context = super(DebtsCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(DebtsCreateView, self).form_valid(form)


class DebtsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Debt
    template_name = 'core/debt_delete.html'
    context_object_name = 'debts'
    success_url = reverse_lazy('core:profile')
    success_message = _('Ваш боржник був успішно Видалений')

    def get_object(self, queryset=None):
        debt_id = int(self.kwargs.get('id'))
        return Debt.objects.get(id=debt_id)

    def test_func(self):
        pass


class DebtsUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Debt
    form_class = DebtForm
    template_name = 'core/debt_update.html'
    context_object_name = 'debt'
    success_message = _('Дані про боржника були успішно змінені')

    def get_context_data(self, **kwargs):
        context = super(DebtsUpdateView, self).get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        debt_id = int(self.kwargs.get('id'))
        return Debt.objects.get(id=debt_id)

    def get_success_url(self):
        return reverse_lazy('core:debt-detail', args=(self.kwargs.get('id'), ))


class DebtsSynchronizeView(View):
    pass


class CategoryCreateView(CreateView):
    pass


class CategoryDeleteView(DeleteView):
    pass
