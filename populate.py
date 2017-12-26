import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cryptoscene.settings')

import django
django.setup()

from cryptodata.models import Data
import pandas as pd 
import csv 

def populate():
    # list of crypt we want to add
    data = []
    with open('model_database.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data.append({"Ids":row[2],"Name":row[3],"Symbol":row[4],"Type":row[5],"Algorithm":row[6],
                        "Proof":row[7],"Icon":row[8],"URL":row[9]})
            #"Description":row[10]}

    data = data[1:250]

    cats = dict()
    for d in data:
        cats.update({d['Name']:[d]})
    
    for key, values in cats.items():
        for p in values:
            ids = p['Ids']
            name = p['Name']
            symbol = p['Symbol']
            types = p['Type']
            algorithm = p['Algorithm']
            proof = p['Proof']
            url = p['URL']
            icon = p['Icon']
            add_cat(ids,name,symbol,types,proof,url,algorithm,icon)

    # Print out the categories we have added
    for c in Data.objects.all():
        print("-{0}".format(str(c)))

def add_cat(ids,name,symbol,types,proof,url,algorithm,icon):
    c = Data.objects.get_or_create(name=name)[0]
    c.ids = ids
    c.name = name
    c.cryptype = types
    c.proof = proof
    c.link = url
    c.symbol = symbol
    c.algorithm = algorithm
    c.icon = icon
    c.save()
    return c

# Execution
if __name__ == '__main__':
    print("Starting population script..")
    populate()





 # Bitcoin = [{'Algorithm': 'N/A',
    #     'Type': 'Coin',
    #     'Description': 'An innovative payment network and a new kind of money.',
    #     'Proof': 'N/A',
    #     'URL': 'https://bitcoin.org/',
    #     'name': 'Bitcoin',
    #     'symbol': 'BTC'}]
    # Ethereum = [{'Algorithm': 'PoW',
    #     'Type': 'Coin',
    #     'Description': 'Blockchain app platform',
    #     'Proof': 'Ethash',
    #     'URL': 'https://www.ethereum.org/',
    #     'name': 'Ethereum',
    #     'symbol': 'ETH'}]
    # BitcoinCash = [{'Algorithm': 'PoW',
    #     'Type': 'Coin',
    #     'Description': 'Peer-to-Peer Electronic Cash',
    #     'Proof': 'SHA256',
    #     'Token': 'No',
    #     'URL': 'https://www.bitcoincash.org/',
    #     'name': 'Bitcoin Cash',
    #     'symbol': 'BCH'}]
    # Iota = [{'Algorithm': 'N/A',
    #     'Type': 'Coin',
    #     'Description': 'the economy of things. The main innovation behind IOTA is the Tangle',
    #     'Proof': 'N/A',
    #     'Token': 'No',
    #     'URL': 'https://iota.org/',
    #     'name': 'IOTA',
    #     'symbol': 'MIOTA'}]
    # Ripple = [{'Algorithm': 'N/A',
    #     'Type': 'Coin',
    #     'Description': 'The world’s only enterprise blockchain solution for global payments',
    #     'Proof': 'N/A',
    #     'Token': 'No',
    #     'URL': 'https://ripple.com/',
    #     'name': 'Ripple',
    #     'symbol': 'XRP'}]
    # cats = {"Bitcoin":Bitcoin,"Ethereum":Ethereum,"BitcoinCash":BitcoinCash,"Iota":Iota,'Ripple':Ripple}
