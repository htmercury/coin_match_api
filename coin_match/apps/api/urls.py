from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^cryptocurrency$', views.CryptoCreate.as_view()),
    url(r'^cryptocurrency/(?P<pk>\d+)$', views.CryptoView.as_view()),
    url(r'^exchange$', views.ExchangeCreate.as_view()),
    url(r'^exchange/(?P<pk>\d+)$', views.ExchangeView.as_view()),
    url(r'^transaction$', views.TransactionCreate.as_view()),
    url(r'^transactiTn/(?P<pk>\d+)$', views.TransactionView.as_view())
]