# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_title',
            field=models.CharField(default=b'Generic Test', max_length=100),
        ),
    ]
