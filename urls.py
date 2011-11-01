from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^index/$', 'stairs.views.index'),
    url(r'^add_programmer/$', 'stairs.views.add_programmer'),
    url(r'^add_pair/(?P<firstProgrammer_id>.+?)/(?P<secondProgrammer_id>.+?)$', 'stairs.views.add_pair'),
    # url(r'^Pair/', include('Pair.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
