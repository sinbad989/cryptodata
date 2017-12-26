from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
# Create your models here.

class Data(models.Model):
    TYPE = (
        ('Coin','Coin'),
        ('Token','Token'),
    )
    
    # DATA OBTAIN VIA WEBSCRAPPING
    name = models.CharField(max_length=255,db_index=True, default='0')
    ids = models.CharField(max_length=255,db_index=True, default='0')
    symbol = models.CharField(max_length=255,db_index=True, default='0')
    cryptype = models.CharField(max_length=255,choices=TYPE,db_index=True,default="NA")
    proof = models.CharField(max_length=255,db_index=True,default='0')
    algorithm = models.CharField(max_length=255,default='0')
    link = models.URLField(blank=True, null=False)
    icon = models.URLField(blank=True, null=False)
    description = models.TextField()
    
    # DATA OBTAIN VIA API
    rank = models.IntegerField(default=9999)
    price = MoneyField(max_digits = 20, decimal_places = 2, default_currency='USD')
    market_cap = MoneyField(max_digits = 20, decimal_places = 2, default_currency='USD')
    available_supply = models.FloatField(default=0)  
    max_supply = models.FloatField(null=True,default=0) 
    percent_change = models.FloatField(null=True,default=0)
   
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


