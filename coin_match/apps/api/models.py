from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=5)
    symbol = models.CharField(max_length=45)
    supply_limit = models.IntegerField()
    founder= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    watchers = models.ManyToManyField(User, related_name= "crypto_preferences")

class Exchange(models.Model):
    name = models.CharField(max_length=255)
    buy_fee= models.CharField(max_length=7)
    sell_fee= models.CharField(max_length=7)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    desc=models.TextField(max_length=500)
    products = models.ManyToManyField(CryptoCurrency, related_name= "suppliers")

class Transaction(models.Model):
    cryptocurrencies = models.ForeignKey(CryptoCurrency, related_name= "trade")
    exchanges = models.ForeignKey(CryptoCurrency, related_name= "past_trades")
    volume = models.DecimalField(max_digits = 20, decimal_places=10)
    buy_price= models.DecimalField(max_digits = 20, decimal_places=10)
    sell_price= models.DecimalField(max_digits = 20, decimal_places=10)
    spot_price= models.DecimalField(max_digits = 20, decimal_places=10)
    created_at= models.DateTimeField(auto_now_add= True)
    time_stamp= models.DateTimeField()
    updated_at= models.DateTimeField(auto_now= True)

    
