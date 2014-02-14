from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
# Autentification system
from django.contrib.auth.decorators import login_required

from messurements.views import PressureListView, WeightListView, PressureWeightView, WeightFormView

from django.contrib import admin
admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^weight/list/$', login_required(WeightListView.as_view()), name="weight-list"),
    url(r'^pressure/list/$', login_required(PressureListView.as_view()), name="pressure-list"),
    url(r'^messurement/add/$', PressureWeightView, name="add_values"),
    # TODO: For some reasons I'm not able to get it running with reverse'
    url(r'^messurement/add/weight/$', login_required(WeightFormView.as_view(template_name='messurements/weight_form.html', success_url='/dashboard/')), name="add_weight"),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^dashboard/$', TemplateView.as_view(template_name='dashboard.html'), name="user_dashboard")
)
