# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20170412_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscore',
            name='test_score',
            field=models.IntegerField(default=0),
        ),
    ]
