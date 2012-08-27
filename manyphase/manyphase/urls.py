from django.conf.urls import patterns, include, url
from frontend.views import construction
from lead.views import addEmail
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manyphase.views.home', name='home'),
    # url(r'^manyphase/', include('manyphase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', construction),
    url(r'^contact/', addEmail),
)
