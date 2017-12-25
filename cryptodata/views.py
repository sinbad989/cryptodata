import json
import requests
import time

from django.shortcuts import render
from .models import Data

# Create your views here.
def data_list(request):
    number_of_data_to_display = 30
    # EXTRACTING DATA FROM API
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit='+str(number_of_data_to_display)
    content = requests.get(url)
    parsed_json = json.loads(content.text)
    # obtaining the top 10 coins of coinmarketcap
    top_ten_ids = [obj['id'] for obj in parsed_json]

    for ids in top_ten_ids:
        url = 'https://api.coinmarketcap.com/v1/ticker/'+str(ids)+'/'
        content = requests.get(url)
        parsed_json = json.loads(content.text)[0]
        p = Data.objects.get(name= parsed_json['name'])
        p.rank = parsed_json['rank']
        p.price = parsed_json['price_usd']
        p.market_cap = parsed_json["market_cap_usd"]
        p.available_supply = (parsed_json["available_supply"])
        p.max_supply = (parsed_json["max_supply"])
        p.percent_change = (parsed_json["percent_change_1h"])
        p.save()

    data = Data.objects.order_by('rank')[:number_of_data_to_display]   
    return render(request,'cryptodata/list.html',{'data':data})

def about(request):
    return render(request,'cryptodata/about.html',{})



























#"""Sometimes it takes a 1001 ways to find the right way""""

 # ids = [cid[0] for cid in Data.objects.values_list('ids')[:10]]
    # for i in ids:
    #     url = 'https://api.coinmarketcap.com/v1/ticker/'+str(i)+'/'
    #     content = requests.get(url)
    #     parsed_json = json.loads(content.text)[0]
    #     p = Data.objects.get(name= parsed_json['name'])
    #     p.rank = parsed_json['rank']
    #     p.price = parsed_json['price_usd']
    #     p.market_cap = obj["market_cap_usd"]
    #     p.available_supply = (obj["available_supply"])
    #     p.max_supply = (obj["max_supply"])
    #     p.save()
    # save the data extracted via API in our database
    # names = [n[0] for n in Data.objects.values_list('name')]
    # for obj in parsed_json:
    #     if obj['name'] in names:
    #         p = Data.objects.get(name= obj['name'])
    #         p.rank = obj['rank']
    #         p.price = obj["price_usd"]
    #         p.market_cap = obj["market_cap_usd"]
    #         p.available_supply = (obj["available_supply"])
    #         p.max_supply = (obj["max_supply"])
    #         p.save()    # save the data extracted via API in our database
    # names = [n[0] for n in Data.objects.values_list('name')]
    # for obj in parsed_json:
    #     if obj['name'] in names:
    #         p = Data.objects.get(name= obj['name'])
    #         p.rank = obj['rank']
    #         p.price = obj["price_usd"]
    #         p.market_cap = obj["market_cap_usd"]
    #         p.available_supply = (obj["available_supply"])
    #         p.max_supply = (obj["max_supply"])
    #         p.save()
