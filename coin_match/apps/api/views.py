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
    if curr1 == "XBT":
        name= "Bitcoin"
        ticker= r.json()['result'][f'X{curr1}Z{curr2}']
    elif curr1 == "BCH":
        name="Bitcoin Cash"
        ticker= r.json()['result'][f'X{curr1}Z{curr2}']
    elif curr1 == "DASH":
        name="Dash"
        ticker= r.json()['result'][f'{curr1}{curr2}']
    elif curr1 == "ETH":
        name= "Ethereum"
        ticker= r.json()['result'][f'X{curr1}Z{curr2}']
    elif curr1 == "LTC":
        name="LiteCoin"
        ticker= r.json()['result'][f'X{curr1}Z{curr2}']
    elif curr1 =="XDG":
        name="Dogecoin"
        ticker= r.json()['result'][f'X{curr1}Z{curr2}']
    elif curr1 =="XRP":
        name="Ripple"
        ticker= r.json()['result'][f'X{curr1}Z{curr2}']
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
    elif curr1 == "bch":
        name="Bitcoin Cash"
    elif curr1 == "eth":
        name= "Ethereum"
    elif curr1 == "ltc":
        name="LiteCoin"
    elif curr1 =="xrp":
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
    volume=float(ticker['volume'][f'{curr1}'.upper()])
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
    if curr1=="BTC":
        name="Bitcoin"
    elif curr1=="ETH":
        name="Ethereum"
    elif curr1=="BCH":
        name="Bitcoin Cash"
    elif curr1== "LTC":
        name="Litecoin"
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
    btc_context={}
    eth_context={}
    bch_context={}
    ltc_context={}
    dash_context={}
    xrp_context={}
    doge_context={}

    if crypto.abbreviation=="BTC":
        btc_context={
            "a": coinsquare_data_retrieval(),
            "b": kraken_data_retrieval("XBT","USD"),
            "c": cex_data_retrieval("BTC","USD"),
            "d": bitstamp_data_retrieval("btc","usd"),
            "e": bitsquare_data_retrieval("btc","usd"),
            "f": localbitcoin_data_retrieval(),
            "g": gemini_data_retrieval("btc","usd"),
            "h": coinbase_data_retrieval("BTC","USD")
        }
    elif crypto.abbreviation=="ETH":
        eth_context={
            "a": coinbase_data_retrieval("ETH","USD"),
            "b": kraken_data_retrieval("ETH","USD"),
            "c": cex_data_retrieval("ETH","USD"),
            "d": bitstamp_data_retrieval("eth","usd"),
            "e": gemini_data_retrieval("eth","usd")
        }
    elif crypto.abbreviation=="BCH":
        bch_context={
            "a": coinbase_data_retrieval("BCH","USD"),
            "b": kraken_data_retrieval("BCH","USD"),
            "c": cex_data_retrieval("BCH","USD"),
            "d": bitstamp_data_retrieval("bch","usd"),
        }
    elif crypto.abbreviation=="LTC":
        ltc_context={
            "a": coinbase_data_retrieval("LTC","USD"),
            "b": kraken_data_retrieval("LTC","USD"),
            "c": bitstamp_data_retrieval("ltc","usd"),
        }
    elif crypto.abbreviation=="DASH":
        dash_context={
            "a": kraken_data_retrieval("DASH","USD"),
            "b": cex_data_retrieval("DASH","USD"),
        }
    elif crypto.abbreviation=="XRP":
        xrp_context={
            "a": kraken_data_retrieval("XRP","USD"),
            "b": cex_data_retrieval("XRP","USD"),
            "c": bitstamp_data_retrieval("xrp","usd")
        }
    elif crypto.abbreviation=="DOGE":
        doge_context={
            "a": kraken_data_retrieval("DOGE","USD")
        }
        
    context={
        "currency":crypto,
        "exchanges":exchanges,
        "btc_context":btc_context,
        "eth_context":eth_context,
        "bch_context":bch_context,
        "ltc_context":ltc_context,
        "dash_context":dash_context,
        "xrp_context":xrp_context,
        "doge_context":doge_context
    }

    return render(request, 'api/show_crypto.html',context)

def show_exchange(request,pk):
    exchange= Exchange.objects.get(id=pk)
    currencies= exchange.products.all()
    cex_context={}
    coinbase_context={}
    coinsquare_context={}
    kraken_context={}
    bitstamp_context={}
    bitsquare_context={}
    local_context={}
    gemini_context={}
    if exchange.name == "Cex.io":
        cex_context={
            "a": cex_data_retrieval("BTC","USD"),
            "b": cex_data_retrieval("ETH","USD"),
            "c": cex_data_retrieval("BCH","USD"),
            "d": cex_data_retrieval("XRP","USD"),
            "e": cex_data_retrieval("DASH","USD"),
        }
    elif exchange.name == "Coinbase":
        coinbase_context={
            "a": coinbase_data_retrieval("BTC","USD"),
            "b": coinbase_data_retrieval("ETH","USD"),
            "c": coinbase_data_retrieval("BCH","USD"),
            # "d": coinbase_data_retrieval("LTC","USD"),
        }
    elif exchange.name=="Coinsquare":
        coinsquare_context={
            "a":coinsquare_data_retrieval()
        }
    elif exchange.name=="Kraken":
        kraken_context={
            "a": kraken_data_retrieval("XBT","USD"),
            "b": kraken_data_retrieval("ETH","USD"),
            "c": kraken_data_retrieval("BCH","USD"),
            "d": kraken_data_retrieval("LTC","USD"),
            "e": kraken_data_retrieval("XRP","USD"),
            "f": kraken_data_retrieval("DASH","USD"),
            "g": kraken_data_retrieval("DOGE","USD"),
        }
    elif exchange.name=="BitStamp":
        bitstamp_context={
            "a": bitstamp_data_retrieval("btc","usd"),
            "b": bitstamp_data_retrieval("eth","usd"),
            "c": bitstamp_data_retrieval("bch","usd"),
            "d": bitstamp_data_retrieval("ltc","usd"),
            "e": bitstamp_data_retrieval("xrp","usd"),
        }
    elif exchange.name=="Bitsquare":
        bitsquare_context={
            "a":bitsquare_data_retrieval("btc","usd")
        }
    elif exchange.name =="Local Bitcoin":
        local_context={
            "a":localbitcoin_data_retrieval()
        }
    elif exchange.name=="Gemini":
        gemini_context={
            "a": gemini_data_retrieval("btc","usd"),
            "b": gemini_data_retrieval("eth","usd")
        }

    context={
        "exchange":exchange,
        "currencies":currencies,
        "cex_context":cex_context,
        "coinbase_context":coinbase_context,
        "coinsquare_context":coinsquare_context,
        "kraken_context":kraken_context,
        "bitstamp_context":bitstamp_context,
        "bitsquare_context":bitsquare_context,
        "local_context":local_context,
        "gemini_context":gemini_context
    }
    return render(request, 'api/show_exchange.html',context)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)