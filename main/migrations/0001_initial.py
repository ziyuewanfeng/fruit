# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buy_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='com_pass',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=__builtin__.id)),
                ('comment', models.CharField(max_length=300)),
                ('buy_user', models.ForeignKey(to='main.buy_user')),
            ],
        ),
        migrations.CreateModel(
            name='people_pass',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sell_user',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('identity_num', models.CharField(max_length=100)),
                ('com_pass', models.ForeignKey(to='main.com_pass')),
            ],
        ),
        migrations.CreateModel(
            name='sell_user_fruit',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=__builtin__.id)),
                ('sell_fruit', models.CharField(max_length=200)),
                ('valuse', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to='main.sell_user')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='sell_user',
            field=models.ForeignKey(to='main.sell_user'),
        ),
        migrations.AddField(
            model_name='com_pass',
            name='people',
            field=models.ForeignKey(to='main.people_pass'),
        ),
    ]
