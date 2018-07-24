from django.test import TestCase
from .models import *
from rest_framework.test import APIClient
from rest_framework import status
from datetime import datetime
from django.core.urlresolvers import reverse

class ExchangeModelTestCase(TestCase):
    def setUp(self):
        self.exchange_name = 'sample_exchange'
        self.exchange_buy_fee = '1%'
        self.exchange_sell_fee = '2%'
        self.exchange_desc = 'an exchange'
        self.exchange = Exchange(name=self.exchange_name, buy_fee=self.exchange_buy_fee, sell_fee=self.exchange_sell_fee, desc=self.exchange_desc)
    def test_model_can_create_an_exchange(self):
        old_count = Exchange.objects.count()
        self.exchange.save()
        new_count = Exchange.objects.count()
        self.assertNotEqual(old_count, new_count)

class ExchangeViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        CryptoCurrency.objects.create(name='pepecoin', abbreviation='pp', symbol='p', supply_limit=1, founder='king pepe')
        self.exchange_data = {
            "name": "sample_exchange",
            "buy_fee": "1%",
            "sell_fee": "2%",
            "desc": "exchange",
            "products": [1],
            "past_trades": []
        }
        self.response = self.client.post(
            '/exchange',
            self.exchange_data,
            format="json"
        )
    def test_api_can_create_an_exchange(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class CryptoCurrencyModelTestCase(TestCase):
    def setUp(self):
        self.cryptocurrency_name = 'pepecoin'
        self.cryptocurrency_abbreviation = 'pp'
        self.cryptocurrency_symbol = 'p'
        self.cryptocurrency_supply_limit = 1
        self.cryptocurrency_founder = 'king pepe'
        self.cryptocurrency = CryptoCurrency(name=self.cryptocurrency_name, abbreviation=self.cryptocurrency_abbreviation, symbol=self.cryptocurrency_symbol, supply_limit=self.cryptocurrency_supply_limit, founder=self.cryptocurrency_founder)
    def test_model_can_create_an_cryptocurrency(self):
        old_count = CryptoCurrency.objects.count()
        self.cryptocurrency.save()
        new_count = CryptoCurrency.objects.count()
        self.assertNotEqual(old_count, new_count)

class CryptoCurrencyViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cryptocurrency_data = {
            "name": "pepecoin",
            "abbreviation": "pp",
            "symbol": "p",
            "supply_limit": 1,
            "founder": "king pepe",
            "trade": []
        }
        self.response = self.client.post(
            '/cryptocurrency',
            self.cryptocurrency_data,
            format="json"
        )
    def test_api_can_create_a_cryptocurrency(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class TransactionModelTestCase(TestCase):
    def setUp(self):
        CryptoCurrency.objects.create(name='pepecoin', abbreviation='pp', symbol='p', supply_limit=1, founder='king pepe')
        Exchange.objects.create(name='sample_exchange', buy_fee='2%', sell_fee='2%', desc='an exchange')
        self.transaction_volume = 42
        self.transaction_buy_price = 11
        self.transaction_sell_price = 12
        self.transaction_spot_price = 10
        self.transaction_time_stamp = datetime.now()
        self.transaction = Transaction(cryptocurrencies=CryptoCurrency.objects.get(id=1), exchanges=Exchange.objects.get(id=1), volume=self.transaction_volume, buy_price=self.transaction_buy_price, sell_price=self.transaction_sell_price, spot_price=self.transaction_spot_price, time_stamp=self.transaction_time_stamp)
    def test_model_can_create_an_transaction(self):
        old_count = Transaction.objects.count()
        self.transaction.save()
        new_count = Transaction.objects.count()
        self.assertNotEqual(old_count, new_count)

class TransactionViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        CryptoCurrency.objects.create(name='pepecoin', abbreviation='pp', symbol='p', supply_limit=1, founder='king pepe')
        Exchange.objects.create(name='sample_exchange', buy_fee='2%', sell_fee='2%', desc='an exchange')
        self.transaction_data = {
            "volume": 42,
            "buy_price": 12,
            "sell_price": 11,
            "spot_price": 10,
            "time_stamp": "2131-12-15T13:31:00Z",
            "cryptocurrencies": 1,
            "exchanges": 1
        }
        self.response = self.client.post(
            '/transaction',
            self.transaction_data,
            format="json"
        )
    def test_api_can_create_an_exchange(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

