from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

# Autentification system
from django.contrib.auth.decorators import login_required

from messurements.views import PressureListView, WeightListView, PressureWeightView, UserProfileCreateView, UserProfileUpdateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^weight/list/$', login_required(WeightListView.as_view()), name="weight-list"),
    url(r'^pressure/list/$', login_required(PressureListView.as_view()), name="pressure-list"),
    url(r'^messurement/add/$', PressureWeightView, name="add_values"),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^dashboard/$', TemplateView.as_view(template_name='dashboard.html'), name="user_dashboard"),
    url(r'^userprofile/new/$', login_required(UserProfileCreateView.as_view()), name="userprofile_new"),
    url(r'^userprofile/update/$', login_required(UserProfileUpdateView.as_view()), name="userprofile_update")
)
