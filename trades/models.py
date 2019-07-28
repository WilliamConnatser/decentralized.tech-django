# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Trades(models.Model):
    #Reject duplicated trades
    class Meta:
        #These columns must be unique (comparison made after column values are combined)
        unique_together = (('exchange', 'trading_pair', 'trade_id'),)
        verbose_name_plural = 'Trades'

    def __str__(self):
        return self.exchange + " " + self.trading_pair + " " + str(self.trade_id)
    time = models.DateTimeField()
    trade_id = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    exchange = models.CharField(max_length=15)
    trading_pair = models.CharField(max_length=12)
