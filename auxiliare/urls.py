from django.contrib.auth import views as auth_views

from django.conf.urls import url

from .views import HomeView, MenuView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = 'aux_home' ),
    url(r'^menu/$', MenuView.as_view(), name = 'aux_menu' ),
    url(r'^accounts/login/$', auth_views.login, name ='aux_login'),
    url(r'^accounts/logout/$', auth_views.logout, name ='aux_logout', kwargs = {'next_page': '/'}),
]