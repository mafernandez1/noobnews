# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-12 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noobnews', '0021_auto_20190312_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='cheats',
            field=models.CharField(default='There is no Cheats available for this game at the moment. If you would like to add more cheats pleae contact one of the system admins who would be more than happy to add cheats for this game. Let the Games contuine. I am writing more words for the sake of writing words lol lol, more words. More words. I love tango, even tho I can not dance, I look like a whale with slipply fish on his feet. ', max_length=1000),
        ),
    ]
