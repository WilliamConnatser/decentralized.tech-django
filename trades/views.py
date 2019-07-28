# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Trades

# Create your views here.
def index(request):
    #return HttpResponse('tradezz')

    trades = Trades.objects.all()
    context = {
        'title': 'Trades',
        'trades': trades
    }
    return render(request,'trades/index.html', context)