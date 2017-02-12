import csv
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
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


def download_csv(request):
    # Example from https://docs.djangoproject.com/en/1.10/howto/outputting-csv/

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users_list.csv"'

    writer = csv.writer(response)
    for user in User.objects.all():
        writer.writerow([user.username, user.birthday.strftime('%Y-%m-%d')])

    return response
