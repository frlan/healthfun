from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

class Weight(models.Model):
    weight = models.FloatField(blank=False, null=False)
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
