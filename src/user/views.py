from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from user.models import CustomUser


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = ''
    context_object_name = ''

    def get_context_data(self, **kwargs):
        pass

    def get_queryset(self):
        return self.queryset


class FriendListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = ''
    context_object_name = ''

    def get_queryset(self):
        return self.queryset


class FriendDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = ''
    context_object_name = ''

    def get_context_data(self, **kwargs):
        pass

    def get_object(self, queryset=None):
        pass


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = ''
    context_object_name = ''

    def get_context_data(self, **kwargs):
        pass


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = ''
    context_object_name = ''
    form_class = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_object(self, queryset=None):
        return super().get_object()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return super().get_success_url()
