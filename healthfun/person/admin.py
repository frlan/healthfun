from django.contrib import admin

# Register your models here.
from person.models import Person

admin.site.register(Person)
