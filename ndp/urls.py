from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'ndp.views.home', name='home'),
    url(r'^about$', 'ndp.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
)
