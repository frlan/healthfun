from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Pressure, Weight

class PressureForm(forms.ModelForm):

    class Meta:
        model = Pressure
        exclude = ('user', 'timestamp', 'comment' )

class WeightForm(forms.ModelForm):

    class Meta:
        model = Weight
        exclude = ('user', 'timestamp', 'comment')
 
