from django.views.generic.base import View
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Avg
from django.contrib.auth.decorators import login_required


# Current time
from django.utils.timezone import now

from messurements.models import Pressure, Weight
from .forms import PressureForm, WeightForm

########################################################################

class PressureListView(View):
    model = Pressure
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Pressure.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date').annotate(avg1=Avg('sys'))
             .annotate(avg2=Avg('dia'))
             )

        return render(request, self.template_name, {'output': qs})

########################################################################

class WeightListView(View):
    model = Weight
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        qs = list(
             Weight.objects.filter(user=request.user)
             .extra({'date':"date(timestamp)"})
             .values('date')
             .annotate(avg1=Avg('weight')))
        return render(request, self.template_name, {'output': qs})

########################################################################

@login_required
def PressureWeightView(request):
    if request.method == 'POST':
       pressure_form = PressureForm(request.POST)
       weight_form = WeightForm(request.POST)
       if all(form.is_valid() for form in [pressure_form, weight_form]):
            record_time = now()
            pressure = pressure_form.save(commit=False)
            pressure.timestamp = record_time
            pressure.user = request.user
            pressure.save()
            print weight_form
            weight = weight_form.save(commit=False)
            weight.timestamp = record_time
            weight.user = request.user
            weight.save()
            return redirect('weight-list')
    else:
        print "else"
        pressure_form = PressureForm()
        weight_form = WeightForm()
    context = {
        'pressure_form': pressure_form,
        'weight_form': weight_form,
    }
    print request
    print context
    return render(request, 'messurement/messurement_form.html', context)
