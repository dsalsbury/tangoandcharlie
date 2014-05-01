from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tangoandcharlie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/roster/$', 'cobra_directory.admin_views.roster', name="roster"),
    url(r'^admin/', include(admin.site.urls)),
)
