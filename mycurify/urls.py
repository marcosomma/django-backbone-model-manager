import backbone

from django.conf.urls import patterns, include, url
from django.contrib import admin

backbone.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_backbone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'tests.views.coursePage', name='coursePage'),

    url(r'^backbone/', include(backbone.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)