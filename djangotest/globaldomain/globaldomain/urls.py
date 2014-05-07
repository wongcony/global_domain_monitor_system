from django.conf.urls import patterns, include, url
from gd.views import search,domain_search_button,ip_search_button
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'globaldomain.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$',search),
    url(r'^domain_search_button/$',domain_search_button),
    url(r'^ip_search_button/$',ip_search_button),
)
