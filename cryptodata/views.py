import json
import requests
import time

from django.shortcuts import render
from cryptodata.models import Data
from cryptodata.filters import DataFilter
from django.core.paginator import Paginator

# Create your views here.
def data_list(request):
    # Number of data to be extracted and saved to the database
    number_of_data_to_extract = 50

    # EXTRACTING DATA FROM API
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit='+str(number_of_data_to_extract)
    content = requests.get(url)
    parsed_json = json.loads(content.text)
    # obtaining the top 10 coins of coinmarketcap
    top_ten_ids = [obj['id'] for obj in parsed_json]

    for ids in top_ten_ids:
        url = 'https://api.coinmarketcap.com/v1/ticker/'+str(ids)+'/'
        content = requests.get(url)
        parsed_json = json.loads(content.text)[0]
        p, created = Data.objects.get_or_create(name= parsed_json['name'])
        p.price = parsed_json['price_usd']
        p.market_cap = parsed_json["market_cap_usd"]
        p.available_supply = (parsed_json["available_supply"])
        p.max_supply = (parsed_json["max_supply"])
        p.percent_change = (parsed_json["percent_change_1h"])
        p.rank = parsed_json['rank']
        p.save()

    #Number of data to post
    # number_of_data_to_display = 10
    
    datalist = Data.objects.order_by('-score')[:50]
    page = request.GET.get('page',1)

    paginator = Paginator(datalist, 10)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request,'cryptodata/data_list.html',{'data':data})

def about(request):
    return render(request,'cryptodata/about.html',{})

def home(request):
    datalist = Data.objects.order_by('rank')[:50]
    page = request.GET.get('page',1)

    paginator = Paginator(datalist, 10)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request,'cryptodata/home.html',{'data':data})

def search(request):
    data_list = Data.objects.all().order_by('rank')
    data_filter = DataFilter(request.GET, queryset=data_list)
    return render(request,'cryptodata/search.html',{'filter':data_filter})













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
