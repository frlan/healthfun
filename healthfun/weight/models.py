from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Weight(models.Model):
    weight = models.FloatField(blank=False, null=False, verbose_name=_(u"Weight"))
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
