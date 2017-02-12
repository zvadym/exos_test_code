from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('exos_test.apps.users.urls')),
]
