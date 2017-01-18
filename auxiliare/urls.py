from django.contrib.auth import views as auth_views

from django.conf.urls import url

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
]