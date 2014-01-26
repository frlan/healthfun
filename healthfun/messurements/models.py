from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Pressure (models.Model):
    user = models.ForeignKey(User)
    sys = models.FloatField(blank=False, null=False, verbose_name=_(u"systolic"))
    dia = models.FloatField(blank=False, null=False, verbose_name=_(u"diastolic"))
    pulse = models.IntegerField(blank=False, null=False, verbose_name=_(u"Pulse"))
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    comment = models.TextField()
    
    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")

class Weight(models.Model):
    user = models.ForeignKey(User)
    weight = models.FloatField(blank=False, null=False, verbose_name=_(u"Weight"))
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    comment = models.TextField()

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
