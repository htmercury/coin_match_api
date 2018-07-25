# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-25 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180725_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='buy_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='spot_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='volume',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
