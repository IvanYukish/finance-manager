from http.client import BAD_REQUEST, OK

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from user.forms import ProfileUpdateForm
from user.models import CustomUser


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    paginate_by = 10


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


class ProfileDetailView(LoginRequiredMixin, DetailView, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'user/profile_detail.html'
    context_object_name = 'user'
    success_url = reverse_lazy('profile')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.is_ajax():
            form = self.get_form()
            if form.is_valid():
                self.form_valid(form)
                return JsonResponse({'status': 'success'}, status=OK)
            else:
                errors = form.errors
                return JsonResponse({"errors": errors}, status=BAD_REQUEST, json_dumps_params={'ensure_ascii': False})

        return render(request, self.template_name, self.get_form())

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['form'] = ProfileUpdateForm(instance=self.get_object())
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'user/profile_update.html'
    context_object_name = 'user'
    form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')
