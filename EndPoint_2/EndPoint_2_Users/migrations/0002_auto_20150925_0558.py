# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EndPoint_2_Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatabase',
            name='profession',
            field=models.CharField(max_length=25, verbose_name=b'Profession'),
        ),
    ]
