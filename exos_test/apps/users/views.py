from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import User


class UserListView(ListView):
    model = User


class UserMixin(object):
    model = User
    fields = (
        'username',
        'birthday'
    )
    success_url = reverse_lazy('users_list')


class UserCreateView(UserMixin, CreateView):
    pass


class UserUpdateView(UserMixin, UpdateView):
    pass


class UserDeleteView(UserMixin, DeleteView):
    pass


class UserDetailView(DetailView):
    model = User
