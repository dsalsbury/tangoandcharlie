from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tangoandcharlie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/$', 'cobra_directory.admin_views.roster', name="roster"),
    url(r'^profile/(?P<user_id>\d+)/$', 'cobra_directory.admin_views.profile', name="profile"),
    url(r'^admin/', include(admin.site.urls)),
)
