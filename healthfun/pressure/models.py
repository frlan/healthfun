from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

class Pressure (models.Model):
    timestamp = models.DateTimeField()
    sys = models.FloatField(blank=False, null=False)
    dia = models.FloatField(blank=False, null=False)
    pulse = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
            
