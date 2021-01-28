from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.views.generic.base import View


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html', {})


class DebtListView(ListView):
    pass


class DebtCreateView(CreateView):
    pass


class DebtDeleteView(DeleteView):
    pass


class DebtUpdateView(UpdateView):
    pass


class DebtSynchronizeView(View):
    pass


class CategoryCreateView(CreateView):
    pass


class CategoryDeleteView(DeleteView):
    pass
