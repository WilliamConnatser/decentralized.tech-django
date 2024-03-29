# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-28 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('trade_id', models.IntegerField()),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('exchange', models.CharField(max_length=15)),
                ('trading_pair', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='trades',
            unique_together=set([('exchange', 'trading_pair', 'trade_id')]),
        ),
    ]
