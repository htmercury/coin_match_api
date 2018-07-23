from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class CryptoView(generics.RetrieveUpdateDestroyAPIView):
    queryset= CryptoCurrency.objects.all()
    serializer_class=CryptoCurrencySerializer