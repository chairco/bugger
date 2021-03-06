# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 05:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buglist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('SW Version', 'SW Version'), ('HartBeat', 'HeartBeat'), ('ErrorCode', 'ErrorCode')], max_length=10, verbose_name='Type')),
                ('station', models.CharField(max_length=20, verbose_name='station')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('content', models.TextField(max_length=2000, null=True, verbose_name='content')),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], max_length=5, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_buglists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Buglists',
                'ordering': ['-created_at'],
                'verbose_name': 'Buglist',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationid', models.CharField(max_length=50, verbose_name='stationid')),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], max_length=5, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buglist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items_station', to='buglists.Buglist', verbose_name='buglist')),
            ],
            options={
                'verbose_name_plural': 'Stations',
                'ordering': ['-created_at'],
                'verbose_name': 'Station',
            },
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300, null=True, verbose_name='message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buglist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items_tracker', to='buglists.Buglist', verbose_name='buglist')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_tracker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Trackers',
                'ordering': ['-created_at'],
                'verbose_name': 'Tracker',
            },
        ),
    ]
