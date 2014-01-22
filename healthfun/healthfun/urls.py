from django.conf.urls import patterns, include, url

from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'healthfun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
