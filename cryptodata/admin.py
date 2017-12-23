from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('name','rank','symbol','price','percent_change','market_cap','cryptype','algorithm','proof')
    
admin.site.register(Data, DataAdmin) 
