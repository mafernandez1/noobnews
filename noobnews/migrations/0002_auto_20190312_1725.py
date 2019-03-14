# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-12 17:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noobnews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ratingValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviews_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('comments', models.CharField(max_length=300)),
                ('publish_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('comment_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile_image', models.ImageField(default='NoProfile.jpg', upload_to='static/profile_images')),
                ('player_tag', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='videogame',
        ),
        migrations.AlterModelOptions(
            name='videogame',
            options={'verbose_name_plural': 'videogames'},
        ),
        migrations.AddField(
            model_name='videogame',
            name='cheats',
            field=models.CharField(default='There are no Cheats available for this game at the moment', max_length=300),
        ),
        migrations.AddField(
            model_name='videogame',
            name='easter_eggs',
            field=models.CharField(default='There are no Easter Eggs available for this game at the moment', max_length=300),
        ),
        migrations.AddField(
            model_name='videogame',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='videogame',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='videogame',
            name='speedRun',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videogame',
            name='trivia',
            field=models.CharField(default='There are no Trivia available for this game at the moment', max_length=300),
        ),
        migrations.AddField(
            model_name='videogame',
            name='youtubeurl',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videogame',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='videogamelist',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noobnews.UserProfile'),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='score',
            name='videogame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noobnews.VideoGame'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noobnews.UserProfile'),
        ),
        migrations.AddField(
            model_name='review',
            name='videogame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noobnews.VideoGame'),
        ),
    ]
