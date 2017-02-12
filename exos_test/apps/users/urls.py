from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UserListView.as_view(), name='users_list'),
    url(r'^create/$', views.UserCreateView.as_view(), name='users_create'),
    url(r'^update/(?P<pk>\d+)/$', views.UserUpdateView.as_view(), name='users_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.UserDeleteView.as_view(), name='users_delete'),
    url(r'^detail/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='users_detail'),
]
