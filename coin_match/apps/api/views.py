from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
import requests
from datetime import datetime
from .serializers import *
from .models import *

class CryptoView(generics.RetrieveUpdateDestroyAPIView):
    queryset= CryptoCurrency.objects.all()
    serializer_class=CryptoCurrencySerializer

class CryptoCreate(generics.ListCreateAPIView):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save()

class ExchangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Exchange.objects.all()
    serializer_class=ExchangeSerializer

class ExchangeCreate(generics.ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save()

class TransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Transaction.objects.all()
    serializer_class=TransactionSerializer

class TransactionCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save()

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
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
    name= "Bitcoin"
    volume = float(ticker['volume'])
    time_stamp= datetime.now()
    buy_price = float(ticker['bid'])
    if ticker['bid'] =='null':
        buy_price= NULL
    sell_price=float(ticker['ask'])
    if ticker['ask'] =='null':
        sell_price= NULL
    spot_price = float(ticker['last'])
    if ticker['last'] =='null':
        spot_price= NULL
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="Coinsquare"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)
    return 

def kraken_data_retrieval(curr1,curr2):
    r= requests.get(f'https://api.kraken.com/0/public/Ticker?pair={curr1}{curr2}')
    ticker= r.json()['result'][f'X{curr1}Z{curr2}']
    if curr1 == "XBT":
        name= "Bitcoin"
    elif curr1 == "BCH":
        name="Bitcoin Cash"
    elif curr1 == "DASH":
        name="Dash"
    elif curr1 == "ETH":
        name= "Ethereum"
    elif curr1 == "LTC":
        name="LiteCoin"
    elif curr1 =="XDG":
        name="Dogecoin"
    elif curr1 =="XRP":
        name="Ripple"
    volume=float(ticker['v'][1])
    time_stamp = datetime.now()
    buy_price=float(ticker['b'][0])
    if ticker['b'][0]=='null':
        buy_price= NULL
    sell_price=float(ticker['a'][0])
    if ticker['a'][0]=='null':
        sell_price= NULL
    spot_price=float(ticker['c'][0])
    if ticker['c'][0]=='null':
        spot_price= NULL
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="Kraken"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)

    return

def cex_data_retrieval(curr1,curr2):
    r= requests.get(f'https://cex.io/api/ticker/{curr1}/{curr2}')
    ticker= r.json()
    if curr1 == "BTC":
        name= "Bitcoin"
    elif curr1 == "BCH":
        name="Bitcoin Cash"
    elif curr1 == "DASH":
        name="Dash"
    elif curr1 == "ETH":
        name= "Ethereum"
    elif curr1 =="XRP":
        name="Ripple"
    volume=float(ticker['volume'])
    time_stamp=datetime.fromtimestamp(int(ticker['timestamp']))
    buy_price=float(ticker['bid'])
    if ticker['bid'] =='null':
        buy_price= NULL
    sell_price=float(ticker['ask'])
    if ticker['ask'] =='null':
        sell_price= NULL
    spot_price=float(ticker['last'])
    if ticker['last'] =='null':
        spot_price= NULL
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="Cex.io"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)
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
    if curr1 == "btc":
        name= "Bitcoin"
    elif curr1 == "BCH":
        name="Bitcoin Cash"
    elif curr1 == "ETH":
        name= "Ethereum"
    elif curr1 == "LTC":
        name="LiteCoin"
    elif curr1 =="XRP":
        name="Ripple"
    volume=float(ticker['volume'])
    time_stamp = datetime.fromtimestamp(int(ticker['timestamp']))
    buy_price=float(ticker['bid'])
    if ticker['bid'] =='null':
        buy_price= NULL
    sell_price=float(ticker['ask'])
    if ticker['ask'] =='null':
        sell_price= NULL
    spot_price=float(ticker['last'])
    if ticker['last'] =='null':
        spot_price= NULL
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="BitStamp"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)
    return 

def bitsquare_data_retrieval(curr1,curr2):
    r= requests.get(f'https://markets.bisq.network/api/ticker?market={curr1}_{curr2}')
    ticker= r.json()[0]
    name="Bitcoin"
    volume=float(ticker['volume_right'])
    time_stamp = datetime.now()
    if ticker['buy'] == None:
        buy_price= 0
    else:
        buy_price=float(ticker['buy'])
    sell_price=float(ticker['sell'])
    if ticker['sell'] =='null':
        sell_price= NULL
    spot_price=float(ticker['last'])
    if ticker['last'] =='null':
        spot_price= NULL
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="Bitsquare"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)
    return 

def localbitcoin_data_retrieval():
    r= requests.get('https://localbitcoins.com/bitcoincharts/usd/trades.json')
    ticker= r.json()[499]
    name= "Bitcoin"
    volume=float(ticker['amount'])
    time_stamp = datetime.fromtimestamp(int(ticker['date']))
    spot_price=float(ticker['price'])
    if ticker['price'] =='null':
        spot_price= NULL
    buy_price=0
    sell_price=0
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="Local Bitcoin"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)
    return 

def gemini_data_retrieval(curr1,curr2):
    r= requests.get(f'https://api.gemini.com/v1/pubticker/{curr1}{curr2}')
    ticker= r.json()
    if curr1== "btc":
        name="Bitcoin"
    elif curr1=="eth":
        name="Ethereum"
    volume=float(ticker['volume']['BTC'])
    time_stamp = datetime.fromtimestamp(int(ticker['volume']['timestamp'])/1000)
    buy_price=float(ticker['bid'])
    if ticker['bid'] =='null':
        buy_price= NULL
    sell_price=float(ticker['ask'])
    if ticker['ask']=='null':
        sell_price= NULL
    spot_price=float(ticker['last'])
    if ticker['last'] =='null':
        spot_price= NULL
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="Gemini"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)
    return 

def coinbase_data_retrieval(curr1,curr2):
    r= requests.get(f'https://api.coinbase.com/v2/prices/{curr1}-{curr2}/spot')
    ticker= r.json()['data']
    name="Bitcoin"
    spot_price=float(ticker['amount'])
    if ticker['amount'] =='null':
        spot_price= NULL
    b = requests.get(f'https://api.coinbase.com/v2/prices/{curr1}-{curr2}/buy')
    ticker2=b.json()['data']
    buy_price=float(ticker2['amount'])
    if ticker2['amount'] =='null':
        buy_price= NULL
    s = requests.get(f'https://api.coinbase.com/v2/prices/{curr1}-{curr2}/buy')
    ticker3=s.json()['data']
    sell_price=float(ticker3['amount'])
    if ticker['amount'] =='null':
        sell_price= NULL
    time_stamp=datetime.now()
    volume=0
    Transaction.objects.create(cryptocurrencies= CryptoCurrency.objects.get(name=name),exchanges= Exchange.objects.get(name="Coinbase"), volume=volume, buy_price=buy_price,sell_price=sell_price,spot_price=spot_price,time_stamp=time_stamp)
    return 

def show_crypto(request, pk):
    crypto= CryptoCurrency.objects.get(id=pk)
    exchanges=crypto.suppliers.all()
    transactions= Transaction.objects.filter(cryptocurrencies=crypto).filter(exchanges=exchanges)
    

    context={
        "currency":crypto,
        "exchanges":exchanges,
    }
    print(coinsquare_data_retrieval())
    print(kraken_data_retrieval("XBT","USD"))
    print(cex_data_retrieval("BTC","USD"))
    print(bitstamp_data_retrieval("btc","usd"))
    print(bitsquare_data_retrieval("btc","usd"))
    print(localbitcoin_data_retrieval())
    print(gemini_data_retrieval("btc","usd"))
    print(coinbase_data_retrieval("BTC","USD"))
    return render(request, 'api/show_crypto.html',context)

def show_exchange(request,pk):
    exchange= Exchange.objects.get(id=pk)
    currencies= exchange.products.all()
    context={
        "exchange":exchange,
        "currencies":currencies
    }
    print(coinsquare_data_retrieval())
    print(kraken_data_retrieval("XBT","USD"))
    print(cex_data_retrieval("BTC","USD"))
    print(bitstamp_data_retrieval("btc","usd"))
    print(bitsquare_data_retrieval("btc","usd"))
    print(localbitcoin_data_retrieval())
    print(gemini_data_retrieval("btc","usd"))
    print(coinbase_data_retrieval("BTC","USD"))
    return render(request, 'api/show_exchange.html',context)
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)