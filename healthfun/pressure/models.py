from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Pressure (models.Model):
    person = models.ForeignKey('person.Person')
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    sys = models.FloatField(blank=False, null=False, verbose_name=_(u"systolic"))
    dia = models.FloatField(blank=False, null=False, verbose_name=_(u"diastolic"))
    pulse = models.IntegerField(blank=False, null=False, verbose_name=_(u"Pulse"))

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")

