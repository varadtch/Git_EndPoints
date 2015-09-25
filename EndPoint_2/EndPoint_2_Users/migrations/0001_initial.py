# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdatabase',
            fields=[
                ('id', models.CharField(max_length=5, serialize=False, verbose_name=b'Emp_ID', primary_key=True)),
                ('username', models.CharField(max_length=10, verbose_name=b'Username')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('profession', models.CharField(max_length=15, verbose_name=b'Profession')),
                ('city', models.CharField(max_length=15, verbose_name=b'City')),
                ('state', models.CharField(max_length=15, verbose_name=b'State')),
            ],
        ),
    ]
