from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Spreads)
admin.site.register(Totals)
admin.site.register(Moneyline)