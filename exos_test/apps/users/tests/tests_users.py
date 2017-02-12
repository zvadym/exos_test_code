from django.core.urlresolvers import reverse
from django.test import TestCase
from ..models import User


class UsersTestCase(TestCase):
    def test_list_get_200(self):
        response = self.client.get(reverse('users_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_get_200(self):
        response = self.client.get(reverse('users_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        self.assertFalse(User.objects.all().exists())
        response = self.client.post(reverse('users_create'), {'username': 'admin', 'birthday': '1995-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(1, User.objects.count())

    def test_update_get_200(self):
        user = User.objects.create(username='admin', birthday='2000-12-12')
        response = self.client.get(reverse('users_update', args=(user.pk,)))
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        user = User.objects.create(username='admin', birthday='2000-12-12')
        response = self.client.post(reverse('users_update', args=(user.pk,)), {
            'username': user.username,
            'birthday': '1999-01-01'
        })
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.birthday.strftime('%Y-%m-%d'), '1999-01-01')

    def test_delete_get_200(self):
        user = User.objects.create(username='admin', birthday='2000-12-12')
        response = self.client.get(reverse('users_delete', args=(user.pk,)))
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        user = User.objects.create(username='admin', birthday='2000-12-12')
        response = self.client.post(reverse('users_delete', args=(user.pk,)), {})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.all().exists())

    def test_detail_get_200(self):
        user = User.objects.create(username='admin', birthday='2000-12-12')
        response = self.client.get(reverse('users_detail', args=(user.pk,)))
        self.assertEqual(response.status_code, 200)
