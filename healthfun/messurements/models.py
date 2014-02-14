from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.ForeignKey(User)
    height = models.IntegerField(blank=True, null=True)
    targetweight =models.IntegerField(blank=True, null=True, 
                    verbose_name= _("Target weight (kg)"),
                    help_text=_("Weight you want to reach in full kg"))

    def get_absolute_url(self):
        return reverse("user_dashboard")
        
    def __unicode__(self):
        return u'-'.join([self.user.username, unicode(self.id)])

class Pressure (models.Model):
    user = models.ForeignKey(User)
    sys = models.FloatField(blank=False, null=False, verbose_name=_(u"systolic"))
    dia = models.FloatField(blank=False, null=False, verbose_name=_(u"diastolic"))
    pulse = models.IntegerField(blank=False, null=False, verbose_name=_(u"Pulse"))
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")

class Weight(models.Model):
    user = models.ForeignKey(User)
    weight = models.FloatField(blank=False, null=False, verbose_name=_(u"Weight"))
    timestamp = models.DateTimeField(verbose_name=_(u"Messurement timestamp"))
    comment = models.TextField(blank=True, null=True)

    # Hidden fields
    # Remember to be also inserted into list of hidden fields on forms/views 
    _bmi = models.FloatField(blank=True, null=True)

    def bmi(self):
        height = UserProfile.objects.get(pk=self.user.id).height
        if height:
            bmi = self.weight / (height **2 ) * 10000
        return bmi
        
    def __unicode__(self):
        return self.timestamp.strftime("%y-%m-%d: %H-%M")
