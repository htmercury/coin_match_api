from django.shortcuts import render
from rest_framework import generics
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