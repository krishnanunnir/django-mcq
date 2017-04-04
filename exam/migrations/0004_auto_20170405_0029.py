# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170405_0013'),
        ('exam', '0003_auto_20170402_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='max_score',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='permitted_for',
            field=models.ForeignKey(default=0, to='authentication.Department'),
        ),
    ]
