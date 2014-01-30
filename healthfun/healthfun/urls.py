from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

# Autentification system
from django.contrib.auth.decorators import login_required, permission_required

from messurements.views import PressureListView, WeightListView, PressureWeightView

from django.contrib import admin
admin.autodiscover()



urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'healthfun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^weight/list/$', login_required(WeightListView.as_view()), name="weight-list"),
    url(r'^pressure/list/$', login_required(PressureListView.as_view()), name="pressure-list"),
    url(r'^messurement/add/$', PressureWeightView, name="add_values"),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^dashboard/$', TemplateView.as_view(template_name='dashboard.html'), name="user_dashboard")
)
