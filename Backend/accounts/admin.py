from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(Enduser)
admin.site.register(ticker)
admin.site.register(nse_bse_stocks)