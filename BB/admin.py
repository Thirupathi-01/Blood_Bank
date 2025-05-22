from django.contrib import admin
from .models import Donor, Request, BloodInventory

admin.site.register(Donor,)
admin.site.register(Request,)
admin.site.register(BloodInventory,)
