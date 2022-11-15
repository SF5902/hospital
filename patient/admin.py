from django.contrib import admin
from .models import patientinfo, bedsinfo
# Register your models here.
admin.site.register(patientinfo)
admin.site.register(bedsinfo)
