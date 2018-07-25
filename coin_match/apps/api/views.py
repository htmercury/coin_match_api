from django.shortcuts import render, HttpResponse
from rest_framework import generics
import requests
import datetime
from .serializers import *
from .models import *

class CryptoView(generics.RetrieveUpdateDestroyAPIView):
    queryset= CryptoCurrency.objects.all()
    serializer_class=CryptoCurrencySerializer

class CryptoCreate(generics.ListCreateAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
    def perform_create(self, serializer):
        serializer.save()

class ExchangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Exchange.objects.all()
    serializer_class=ExchangeSerializer

class ExchangeCreate(generics.ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    def perform_create(self, serializer):
        serializer.save()

class TransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Transaction.objects.all()
    serializer_class=TransactionSerializer

class TransactionCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    def perform_create(self, serializer):
        serializer.save()

def index(request):
    r= requests.get('https://coinsquare.com/api/v1/data/quotes')

    print(coinsquare_data_retrieval())
    print(kraken_data_retrieval("XBT","USD"))
    print(cex_data_retrieval("BTC","USD"))
    print(bitstamp_data_retrieval("btc","usd"))
    print(bitsquare_data_retrieval("btc","usd"))
    print(localbitcoin_data_retrieval())
    print(gemini_data_retrieval("btc","usd"))
    print(coinbase_data_retrieval("BTC","USD"))

    return HttpResponse("hi")

def coinsquare_data_retrieval():
    r= requests.get('https://coinsquare.com/api/v1/data/quotes')
    ticker= r.json()['quotes'][1]
    print(ticker)
    name= ticker['base']
    volume = ticker['volume']
    time_stamp= datetime.datetime.now()
    buy_price = ticker['bid']
    sell_price=ticker['ask']
    spot_price = ticker['last']
    return 

def kraken_data_retrieval(curr1,curr2):
    r= requests.get(f'https://api.kraken.com/0/public/Ticker?pair={curr1}{curr2}')
    ticker= r.json()['result']['XXBTZUSD']
    name= "BTC"
    volume=ticker['v']
    time_stamp = datetime.datetime.now()
    buy_price=ticker['b']
    sell_price=ticker['a']
    spot_price=ticker['c']
    return

def cex_data_retrieval(curr1,curr2):
    r= requests.get(f'https://cex.io/api/ticker/{curr1}/{curr2}')
    ticker= r.json()
    name="BTC"
    volume=ticker['volume']
    time_stamp=ticker['timestamp']
    buy_price=ticker['bid']
    sell_price=ticker['ask']
    spot_price=ticker['last']
    return 

# def poloniex_data_retrieval():
#     r= requests.get('https://poloniex.com/public?command=returnTicker')
#     ticker= r.json()
#     name= "BTC"
#     volume=ticker['v']
#     time_stamp = datetime.datetime.now()
#     buy_price=ticker['b']
#     sell_price=ticker['a']
#     spot_price=['c']
#     return

def bitstamp_data_retrieval(curr1,curr2):
    r= requests.get(f'https://www.bitstamp.net/api/v2/ticker/{curr1}{curr2}')
    # r= requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd')
    ticker= r.json()
    name="BTC"
    volume=ticker['volume']
    time_stamp = ticker['timestamp']
    buy_price=ticker['bid']
    sell_price=ticker['ask']
    spot_price=ticker['last']
    return 

def bitsquare_data_retrieval(curr1,curr2):
    r= requests.get(f'https://markets.bisq.network/api/ticker?market={curr1}_{curr2}')
    ticker= r.json()[0]
    name= "BTC"
    volume=ticker['volume_right']
    time_stamp = datetime.datetime.now()
    buy_price=ticker['buy']
    sell_price=ticker['sell']
    spot_price=ticker['last']
    return 

def localbitcoin_data_retrieval():
    r= requests.get('https://localbitcoins.com/bitcoincharts/usd/trades.json')
    ticker= r.json()[499]
    name= "BTC"
    volume=ticker['amount']
    time_stamp = ticker['date']
    spot_price=ticker['price']
    buy_price=''
    sell_price=''
    return 

def gemini_data_retrieval(curr1,curr2):
    r= requests.get(f'https://api.gemini.com/v1/pubticker/{curr1}{curr2}')
    ticker= r.json()
    name= "BTC"
    volume=ticker['volume']['BTC']
    time_stamp = ticker['volume']['timestamp']
    buy_price=ticker['bid']
    sell_price=ticker['ask']
    spot_price=ticker['last']
    return 

def coinbase_data_retrieval(curr1,curr2):
    r= requests.get(f'https://api.coinbase.com/v2/prices/{curr1}-{curr2}/spot')
    ticker= r.json()['data']
    name=ticker['base']
    spot_price=ticker['amount']
    b = requests.get(f'https://api.coinbase.com/v2/prices/{curr1}-{curr2}/buy')
    ticker2=b.json()['data']
    buy_price=ticker2['amount']
    s = requests.get(f'https://api.coinbase.com/v2/prices/{curr1}-{curr2}/buy')
    ticker3=s.json()['data']
    sell_price=ticker3['amount']
    time_stamp=datetime.datetime.now()
    volume=""
    return 


    # buy_price= models.DecimalField(max_digits = 20, decimal_places=10)
    # sell_price= models.DecimalField(max_digits = 20, decimal_places=10)
    # spot_price= models.DecimalField(max_digits = 20, decimal_places=10)
    # created_at= models.DateTimeField(auto_now_add= True)
    # time_stamp= models.DateTimeField()
    # updated_at= models.DateTimeField(auto_now= True)