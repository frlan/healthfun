from django.contrib import admin

# Register your models here.
from messurements.models import Pressure, Weight, UserProfile

admin.site.register(Pressure)
admin.site.register(Weight)
admin.site.register(UserProfile)
