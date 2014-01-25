from django.views.generic.base import View
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Avg

from messurements.models import Pressure, Weight


class PressureListView(View):
    model = Pressure
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Pressure.objects.filter(user=1)
             .extra({'date':"date(timestamp)"})
             .values('date').annotate(avg1=Avg('sys'))
             .annotate(avg2=Avg('dia'))
             )

        return render(request, self.template_name, {'output': qs})

class WeightListView(View):
    model = Weight
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Weight.objects.filter(user=1)
             .extra({'date':"date(timestamp)"})
             .values('date')
             .annotate(avg1=Avg('weight')))
        return render(request, self.template_name, {'output': qs})

