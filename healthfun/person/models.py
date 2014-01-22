from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Person(models.Model):
    first_name = models.CharField(verbose_name=_(u"First Name"), max_length=75, blank=True)
    last_name = models.CharField(verbose_name=_(u"Last Name"), max_length=75, blank=True)
    height = models.IntegerField(blank=True)
    email = models.EmailField()

    def __unicode__ (self):
        return self.email
