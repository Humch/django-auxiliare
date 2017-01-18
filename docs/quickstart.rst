Prerequisites
===============

Installing
============

Install the apps with pip ::

    $ pip install django-auxiliare

Configure your settings file
-------------------------------

Add django-auxiliare to your installed_apps ::

    INSTALLED_APPS = [
        ...
        'auxiliare',
    ]

Configure your urls file
-----------------------------

Add django-auxiliare to urls file ::

    from django.conf.urls import url, include
    from auxiliare import urls
    ...
    urlpatterns = [
        ...
        url(r'^', include('auxiliare.urls')),
    ]

