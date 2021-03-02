from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from user.forms import ProfileUpdateForm
from user.models import CustomUser


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.all()


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
    template_name = 'user/profile_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'user/profile_update.html'
    context_object_name = 'user'
    form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')
